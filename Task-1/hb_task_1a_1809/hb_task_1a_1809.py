########################################################################################################################
########################################## eYRC 23-24 Hologlyph Bots Task 1A ###########################################
# Team ID: 1809
# Team Leader Name: Pooja Ramani
# Team Members Name: Kaushal Bhanderi , Jalay Movaliya , Yash Nasit
# College: Chandubhai S. Patel Institute of Technology
########################################################################################################################

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
import math

class CircleTurtles(Node):
    def __init__(self):
        super().__init__("task_1a_1809")
        self.turtle1_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.turtle2_publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_turtles)
        self.angular_velocity1 = 2.0
        self.linear_velocity1 = 2.0
        self.angular_velocity2 =-2.0
        self.linear_velocity2 = 3.0
        self.completed_circle_turtle1 = False
        self.completed_circle_turtle2 = False

        self.odom_subscription_turtle1 = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.odom_callback_turtle1,
            10
        )
        self.odom_subscription_turtle2 = self.create_subscription(
            Pose,
            'turtle2/pose',
            self.odom_callback_turtle2,
            10
        )

        self.odom_data_turtle1 = None
        self.odom_data_turtle2 = None
        self.distance_traveled_turtle1 = 0.0
        self.distance_traveled_turtle2 = 0.0

        self.spawn_turtle1()


    def move_turtles(self):
        self.move_turtle1()
        if self.completed_circle_turtle1:
            self.spawn_turtle2()
        self.move_turtle2()

    def move_turtle1(self):
        if not self.completed_circle_turtle1:
            twist_msg = Twist()
            twist_msg.linear.x = self.linear_velocity1
            twist_msg.angular.z = self.angular_velocity1
            self.turtle1_publisher.publish(twist_msg)
        else:
            twist_msg = Twist()  
            self.turtle1_publisher.publish(twist_msg)

    def move_turtle2(self):
        if not self.completed_circle_turtle2:
            twist_msg = Twist()
            twist_msg.linear.x = self.linear_velocity2
            twist_msg.angular.z = self.angular_velocity2
            self.turtle2_publisher.publish(twist_msg)
        else:
            twist_msg = Twist()  
            self.turtle2_publisher.publish(twist_msg)

    def spawn_turtle1(self):
            client = self.create_client(Spawn, 'spawn')
            request = Spawn.Request()
            request.x = 5.197917
            request.y = 5.197917
            request.theta = 0.0
            request.name = 'turtle1'
       
    def spawn_turtle2(self):
            client = self.create_client(Spawn, 'spawn')
            request = Spawn.Request()
            request.x = 5.197917 
            request.y = 5.197917
            request.theta = 0.0
            request.name = 'turtle2'
            response = client.call_async(request)


    def odom_callback_turtle1(self, msg):
        if not self.completed_circle_turtle1:
            if self.odom_data_turtle1 is not None:
                delta_x = msg.x - self.odom_data_turtle1.x
                delta_y = msg.y - self.odom_data_turtle1.y
                delta_distance = ((delta_x ** 2) + (delta_y ** 2)) ** 0.5
                self.distance_traveled_turtle1 += delta_distance
                self.odom_data_turtle1 = msg
            else:
                self.odom_data_turtle1 = msg

            desired_distance = 2 * math.pi * 1.0

            if self.distance_traveled_turtle1 >= desired_distance:
                self.completed_circle_turtle1 = True

    def odom_callback_turtle2(self, msg):
        if not self.completed_circle_turtle2:
            if self.odom_data_turtle2 is not None:
                delta_x = msg.x - self.odom_data_turtle2.x
                delta_y = msg.y - self.odom_data_turtle2.y
                delta_distance = ((delta_x ** 2) + (delta_y ** 2)) ** 0.5
                self.distance_traveled_turtle2 += delta_distance
                self.odom_data_turtle2 = msg
            else:
                self.odom_data_turtle2 = msg

            desired_distance = 2 * math.pi * 1.5

            if self.distance_traveled_turtle2 >= desired_distance:
                self.completed_circle_turtle2 = True

def main(args=None):
    rclpy.init(args=args)
    node = CircleTurtles()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
