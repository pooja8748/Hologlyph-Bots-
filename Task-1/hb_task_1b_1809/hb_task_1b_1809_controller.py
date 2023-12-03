import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseArray
from nav_msgs.msg import Odometry
import math
from tf2_ros import TransformListener, Buffer
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal

class HBTask1BController(Node):

    def __init__(self):
        super().__init__('controller')
        self.x_goal = 0.0
        self.y_goal = 0.0
        self.theta_goal = 0.0
        self.hb_x = 0.0
        self.hb_y = 0.0
        self.hb_theta = 0.0
        self.odom_msg = None

        self.x_goals = [0, 4, -4, -4, 4]
        self.y_goals = [0, 4, 4, -4, -4]
        self.theta_goals = [0, 1.567, -1.31, -3.213, 0]

        # Initialize Publisher and Subscriber
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odometry_callback,
            10
        )
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.goal_sub = self.create_subscription(
            PoseArray,
            'task1_goals',
            self.task1_goals_callback,
            10
        )

        # Declare a Twist message
        self.vel = Twist()
        # Initialize the required variables to 0

        # For maintaining control loop rate.
        self.rate = self.create_rate(100)
        # Initialize variables that may be needed for the control loop
        self.kp_lin= 0.8
        self.kp_ang= 0.6
        self.dist_tole = 0.7
        self.theta_tole = 0.0014
        self.count = 0.0
        self.goal_index = 0  # Initialize the goal index

        # Create a client to call the NextGoal service
        self.get_next_goal_client = self.create_client(NextGoal, 'next_goal')

    def odometry_callback(self, msg):
        # Extract robot's current position and orientation from the Odometry message
        self.hb_x = msg.pose.pose.position.x
        self.hb_y = msg.pose.pose.position.y
        _, _, self.hb_theta = euler_from_quaternion([
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w
        ])
        # Store the Odometry message
        self.odom_msg = msg

    def task1_goals_callback(self, msg):
        self.x_goals.clear()
        self.y_goals.clear()
        self.theta_goals.clear()
        for waypoint_pose in msg.poses:
            self.x_goals.append(waypoint_pose.position.x)
            self.y_goals.append(waypoint_pose.position.y)
            orientation_q = waypoint_pose.orientation
            orientation_list = [
                orientation_q.x,
                orientation_q.y,
                orientation_q.z,
                orientation_q.w
            ]
            (_, _, theta_goal) = self.quaternion_to_euler(
                orientation_list[0], orientation_list[1],
                orientation_list[2], orientation_list[3])
            self.theta_goals.append(theta_goal)

    def quaternion_to_euler(self, x, y, z, w):
        # Convert quaternion to Euler angles
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw = math.atan2(t3, t4)

        return roll, pitch, yaw
    
    def calculate_errors(self):
        # Calculate errors in global frame
        x_error = self.x_goal- self.hb_x
        y_error = self.y_goal - self.hb_y
        theta_error = self.theta_goal - self.hb_theta

        # Calculate errors in robot body frame
        linear_error = x_error * math.cos(self.hb_theta) + y_error * math.sin(self.hb_theta)
        angular_error = theta_error

        return linear_error, angular_error

    def p_controller(self):
        # Call the service to get the next goal
        next_goal = self.call_get_next_goal()

        if next_goal is not None:
            # Extract goal values from the response
            self.x_goal = next_goal.x_goal
            self.y_goal = next_goal.y_goal
            self.theta_goal = next_goal.theta_goal

            # Calculate errors
            linear_error, angular_error = self.calculate_errors()

            # P control law for linear velocity
            self.vel.linear.x = self.kp_lin * linear_error

            # P control law for angular velocity
            self.vel.angular.z = self.kp_ang * angular_error

            # Check if the robot is close enough to the current goal
            if abs(linear_error) < self.dist_tole and abs(angular_error) < self.theta_tole:
                # Move to the next goal
                self.goal_index = (self.goal_index + 1) % len(self.x_goals)

    def call_get_next_goal(self):
        # Create a request message
        request = NextGoal.Request()

        # Call the service and wait for a response
        while not self.get_next_goal_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

        future = self.get_next_goal_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            return future.result()
        else:
            self.get_logger().error('Service call failed')
            return None

def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the HBTask1BController class
    controller = HBTask1BController()

    # Main loop
    while rclpy.ok():
        # Check if the Odometry message is available
        if controller.odom_msg is not None:
            controller.calculate_errors()
            controller.p_controller()

        # Publish the calculated velocity command
        controller.pub.publish(controller.vel)

        # Spin once to process callbacks
        rclpy.spin_once(controller)

    # Destroy the node and shut down ROS
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()