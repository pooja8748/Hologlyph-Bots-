## Task 1

## Task 1A
Task 1A is a relatively simple task designed just for you to get comfortable with the usage of ROS2

  ## Problem Statement

Create a simple controller for turtlesim using python and use it to perform the desired maneuver with 2 turtles (or e-YAN???) exactly as described below.

There are three things that need to be done:

First, draw a circle with the first turtle.

When the first circle is drawn, the controller node must stop the first turtle and call a service to spawn another turtle.

Lastly, the second turtle should draw another circle bigger than the previous one and stop when it is drawn.

The final output/drawing should resemble the appearance of a snowman.⛄
The expected output for Task 1A is given below 👇 :


![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/138d5113-37f5-436d-b0a8-7e315a5b9e89)


  ## Approach

So how shall we go about implementing task 1A?

Let's complete the following steps one by one:
Step 1: Creating a ROS2 Workspace
Since we will be working with custom packages and customised nodes, we will be creating a workspace where all our changes get incorporated at once when we source the specific workspace. We recommend to create a directory named eyrc_hb where all your different ROS2 workspaces will reside. (Yes, we will have a different workspaces for different tasks)
Now open the terminal and run the following commands step by step:

```bash
sudo apt update
```
```bash
cd
```
Create a new folder eyrc_hb and create another folder named hb_task1a_ws which will be our workspace.

(in -p mode, mkdir command creates the parent directories if not already created)
```bash
mkdir -p eyrc_hb/hb_task1a_ws/src 
```
Navigate to the workspace folder
```bash
cd eyrc_hb/hb_task1a_ws
```
Build a workspace. After this command, your hb_task1a_ws will become a ROS2 workspace.
```bash
colcon build --symlink-install
```
Step 2: Creating a new package inside the ROS2 Workspace
Now navigate to the src folder using cd src inside the workspace and run the following command:
```bash
 ros2 pkg create --build-type ament_python hb_task_1a
```
Now you have successfully created a new package. As you learnt in the ros2 learning resources, in this package we will create the task_1a node that will be called to perform the desired task!

To create the node, navigate to the hb_task_1a folder inside /src/hb_task_1a and run the following commands:
```bash
touch task_1a_<team_id>.py
```
```bash
chmod +x task_1a_<team_id>.py
```
where <team_id> is the is your team ID. For example, if your team ID is 9999, you should create the file names task_1a_9999.py.
Do not usse 9999 as your team ID, this is just an example

The touch command creates a python file and the chmod command converts it into an executable.

Before you continue to build the package further, download the following .zip file and extract it in the src folder of your workspace.

TurtleSim Customized package (ros_tutorials.zip)
Step 3: Editing the task_1a_9999.py file
Open the task_1a_9999.py file in your favourite code editor. (We highly recommend VS Code!)

Now edit the task_1a_9999.py file and implement your logic. We have provided an example in learning resources to get you thoroughly acquainted.

Refer to ROS2 Publisher-Subscriber and Service Example (Python)

Do not forget to add the dependencies in the package.xml file and add the new nodes in the setup.py file inside the 'console scripts' : [] list inside the entry_points dictionary!

You can refer this document for reference- ROS2 Wiki: Creating a Package

And remember to always save your changes!!
```bash
########################################################################################################################
########################################## eYRC 23-24 Hologlyph Bots Task 1A ###########################################
# Team ID:
# Team Leader Name:
# Team Members Name:
# College:
########################################################################################################################
```

## Task 1B

The objective of this task is:

to explore and understand Gazebo-ROS, URDF,
to understand manual control of “high-level model” of a generic holonomic robot (using Planar Move Plugin),
and implement some simple controller on a holonomic drive robot (for ex: 3 P controllers).

  ## Some Motivation
Before we get to controlling a team of three holonomic robots, a prior major milestone will be to control one holonomic drive robot to do the desired task. This will require us to understand and implement the following essential building blocks:

Designing position control of Holonomic Drive Robot (ground vehicle). (this will be done on a “high-level” model of the robot as mentioned above in Task 1B objective).
Understanding forward and inverse kinematics of three-omni-wheeled bot. (the holonomic drive robot that we shall use in this theme)
We’ll only need to implement inverse kinematics, for the purpose of taking the output of the above mentioned controller and controlling the three wheel velocities to achieve the desired (v_x, v_y, w)
Localisation of the robot. In task 1b we’ll build the position control with localisation given (for free) by the simulator. But in the real world (outside simulator) we’ll need to worry about how to localise the robot (i.e. answering the question: where is the robot?), using some sensors (in our case it will be an overhead camera).
At an even higher level than the controller (discussed above) is the question of where to even go? We could call this “Planning”.
If we wish to draw smooth shapes simple position control may not suffice. Therefore we may need to explore more fancy/advanced ideas in control.
All of the above can be implemented directly in hardware, but it is a good idea to simulate and find problems without actually breaking some hardware :stuck_out_tongue:. Here comes Gazebo Simulator and ROS.
In task 1b we shall explore the first and last (6th) points listed above. In task 2a we shall look at the 2nd and 3rd points. In tasks after 2a we shall look at point 4, 5 and also all the points (not mentioned here) related to multi-robot systems

  ## Problem Statement
Implement a simple controller to make the simulated robot (simplified) go to a series of desired pose given ideal localisation.

There are quite a few things that are happening in the highly condense statement above. (So let’s read between the lines :😛

simulated robot (simplified)
first we shall manual actuate the simulated robot
(simplified): by using planar move gazebo model plugin.
Meaning we shall directly control the chassis velocities (v_x, v_y, w) - linear velocities v_x, v_y and angular velicity w, instead of controlling wheel velocities (v1, v2, v3). How these two are related (i.e. kinematics) will be explained in task 2.
go-to-pose controller - given ideal localisation
extend the above code to handle a series of desired poses
The gif below is a demo/example of what one should be able to do at the end of Task 1. Note that there are many shapes that the bot can make, so don't worry if your output isn't exactly same as the example provided. (more about it later...)
Basically there are a lot “cheats” available to us :stuck_out_tongue: because we are working in a simulator. To do the same task in real life we will have to add quite a few more layers, which we shall in future tasks.


![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/b3b38287-3469-4349-a58c-ada7a9ca2cdd)

  ## Approach
So how shall we tackle Task 1B?

Let’s look at the check list above and work on it one by one.

Step 1: Gazebo and URDF

simulated robot
manual actuation of the simulated robot
also get ideal localisation
Step 2: controller.py

Step 2A: go-to-goal-pose controller

given ideal localisation and simplified actuation from step 1.
Step 2B: go-to sequence of goal-poses

Just extend (add some logic) to the above code to handle a series of desired poses.

## Creating a Luanch File and Setuo

For the complete execution of task 1B, there are 2 python files that need to be run simultaneously. Launch files makes it easier by running them using a single command. The 2 files are controller.py and service_node.py.

First, lets create a launch file. Follow the steps given below:

Navigate to the launch folder and create a file named hb_task1b.launch.py.

The launch file name needs to end with launch.py to be recognized and autocompleted by ros2 launch. Your launch file should define the generate_launch_description() function which returns a launch.LaunchDescription() to be used by the ros2 launch verb.

Change this python file into an executable using the following command:
```bash
chmod +x hb_task1b.launch.py
```
Launch File Structure
```bash
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    ld = LaunchDescription()
    controller_node = Node(
        package="<your_package_name>",           # Enter the name of your ROS2 package
        executable="<your_executable_name>",    # Enter the name of your executable
    )
    service_node = Node(
        package="<your_package_name>",           # Enter the name of your ROS2 package
        executable="<your_executable_name>",    # Enter the name of your executable
    )
```
  ## Installing Dependencies

There are many dependencies that are needed to be installed for seamlessly running our Gazebo simulator.

Run the following commands in terminal:
```bash
sudo apt install ros-humble-tf-transformations
sudo pip3 install transforms3d
sudo apt install -f ros-humble-gazebo-ros-pkgs
```

Given below should be the structure of your package.

```bash
Package (hb_task_1b)
    - hb_task_1b
        - __init__.py
    - launch
        - gazebo.launch.py
        - hb_task1b.launch.py
    - urdf
        - hb_bot.urdf.xacro
        - materials.xacro
    - world
        - gazebo.world
    - scripts
        - controller.py
        - service_node.py
    - meshes
        - base.dae
        - wheel.stl
        - 17eyantra_logo_large e.png
```
Now, download the given packages and create the directory structure as mentioned above with the given downloadables.

Once your directory structure is created, navigate to the workspace (hb_task1b_ws) folder, build it using colcon build command and source it using source install/setup.bash command.

Now, launch gazebo:
```bash
ros2 launch hb_task_1b gazebo.launch.py
```
Gazebo will launch and you will see the output similar to the image below.

![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/364ddb65-314f-4173-836b-e524344f2caa)

Now, open another terminal (don't forget to source it) and run the following command for launching the controller and service nodes.
```bash
ros2 launch hb_task_1b hb_task1b.launch.py
```
The expected output is shown below.

![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/a2aff3c6-eebd-4ef1-80e1-17488ff3b6e5)

  ## Controller
Well done on making it to Step 2 of Task 1B! So now that we’ve,

created an urdf file,
launched gazebo, spawned the robot and
are able to actuate it manually
In step 2, Let’s automate the robot, by creating a controller rospy node that will make the robot automatically go to desired goal pose (pose, refers to the position AND orientation of the robot).

 ## Introduction
 go-to-goal controller
given ideal localisation and simplified kinematics from step 1.
skipping/simplified localisation: The odom topic (as declared in the urdf file) is directly giving us the present pose of the robot. Which is not the case in real world. We will eventually use a marker and openCV to localise the robot in a more realistic way. [localise: to answer “Where the Robot is?”, specifically, what is the present (x, y, theta) of the robot.]

skipping/simplified kinematics: The controller we are designing, outputs something like [v_x, v_y, omega] that is sent to cmd_vel, which independently controls the velocities of chassis directly. But in hardware, we are not directly actuating the chassis by giving [v_x, v_y, w], but we give wheel velocities, which is [v_1, v_2, v_3] for a three omni-wheeled robot. We are skipping the problem of finding [v_1, v_2, v_3] given [v_x, v_y, w].

These topics will be covered in Task 2

So what is Holonomic Drive?

An object in the physical “3D” space we live in has 6 Degreed of Freedom.

3 translations, 3 rotations.
An object on a “2D” plane has 3 Degreed of freedom:

2 translations and 1 rotation.
In our convention, it will be translation in the X and Y axis and rotation about the Z axis.
Ground vehicles live on a plane.
The popular differential drive robot has a Non Holonomic CONSTRAINT. That doesn’t allow the robot to translate in one of the axis (say X). This is a constraint on velocity and NOT a constraint on position. So although a differential drive CAN parallel park it has to make many complex manoeuvres to achieve it. While a holonomic drive (ex: Omni wheel robot) can simply translate in that direction (X) since it has no such constraint in that direction.

I.E. The ground vehicle can directly control velocities in ALL the 3 Degrees of Freedom possible.
I.E. Control [v_x, v_y, w] linear velocity in X-Y and Omega: angular velocity in the Z axis. (Unlike only two, [v, w] (or [v_y, w] in our convention) for a differential drive robot.)

The above block of explanation might now give you some clarity on what is holonomic drive.

This leaves one more major question unanswered: What is Forward and Inverse Kinematics? In our specific case of three-omni-wheeled robot, We could simplify it by saying, it’s the relationship between [v_1, v_2, v_3] and [v_x, v_y, w] That’s all for now, more about this in Task 2!

Enough chit-chat, let’s get down to business!

  ## The Task
 So continuing from where we left off in Step1. We now have a launch file which opens gazebo, empty world and spawns the robot.

If you do that and then do rostopic list, you should find two topic of interest:

/cmd_vel
/odom
which are defined in the urdf file, gazebo plugin.

Now we shall create a rospy node: controller.py that will

subscribe to /odom and
publish to /cmd_vel
So in your package directory, create a your_package_name/scripts/ directory and create a file name controller.py inside it.

Now let’s start writing the controller.py file.

We’ll need to import the following modules:
```bash
#!/usr/bin/env python3
import rclpy                                          # ROS 2 Python library for creating ROS 2 nodes
from rclpy.node import Node                           # Node class for creating ROS 2 nodes
from geometry_msgs.msg import Twist                   # Publishing to /cmd_vel with msg type: Twist
from nav_msgs.msg import Odometry                     # Subscribing to /odom with msg type: Odometry
import time                                           # Python time module for time-related functions
import math                                           # Python math module for mathematical functions
from tf.transformations import euler_from_quaternion  # Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle
from my_robot_interfaces.srv import NextGoal          # Service
```
We’ll need some variables to keep track of pose of the robot, x, y, theta.
```bash
self.hb_x = 0
self.hb_y = 0
self.hb_theta = 0
```
We’ll need a callback function for subscribing to /odom. As you must be aware by now, this function will be automatically called everytime to update the pose of the robot (whenever there is an update in the /odom topic).
```bash
def odometryCb(msg):
    global hb_x, hb_y, hb_theta

    # Write your code to take the msg and update the three variables
```
ROS2 Odometry documentation is given here for reference.

Have a look at the data structure of the msg received as argument (Odometry message) and figure out how to get hb_x, hb_y and hb_theta from that.

Hint: You only need to look at the pose part of the data.
```bash
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import math
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal

class HBTask1BController(Node):

   def __init__(self):
        super().__init__('hb_task1b_controller')
        
        # Initialze Publisher and Subscriber
        # We'll leave this for you to figure out the syntax for
        # initialising publisher and subscriber of cmd_vel and odom respectively

        # Declare a Twist message
        self.vel = Twist()
        # Initialise the required variables to 0

        # For maintaining control loop rate.
        self.rate = self.create_rate(100)
        # Initialise variables that may be needed for the control loop
        # For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
        # and also Kp values for the P Controller


        # client for the "next_goal" service
        self.cli = self.create_client(NextGoal, 'next_goal')      
        self.req = NextGoal.Request() 
        self.index = 0

   def main(args=None):
    rclpy.init(args=args)
    
    # Create an instance of the EbotController class
    ebot_controller = HBTask1BController()
   
    # Send an initial request with the index from ebot_controller.index
    ebot_controller.send_request(ebot_controller.index)
    
    # Main loop
    while rclpy.ok():

        # Check if the service call is done
        if ebot_controller.future.done():
            try:
                # response from the service call
                response = ebot_controller.future.result()
            except Exception as e:
                ebot_controller.get_logger().infselfo(
                    'Service call failed %r' % (e,))
            else:
                #########           GOAL POSE             #########
                x_goal      = response.x_goal
                y_goal      = response.y_goal
                theta_goal  = response.theta_goal
                ebot_controller.flag = response.end_of_list
                ####################################################

                # Find error (in x, y and theta) in global frame
                # the /odom topic is giving pose of the robot in global frame
                # the desired pose is declared above and defined by you in global frame
                # therefore calculate error in global frame

                # (Calculate error in body frame)
                # But for Controller outputs robot velocity in robot_body frame, 
                # i.e. velocity are define is in x, y of the robot frame, 
                # Notice: the direction of z axis says the same in global and body frame
                # therefore the errors will have have to be calculated in body frame.
                # 
                # This is probably the crux of Task 1, figure this out and rest should be fine.

                # Finally implement a P controller 
                # to react to the error with velocities in x, y and theta.

                # Safety Check
                # make sure the velocities are within a range.
                # for now since we are in a simulator and we are not dealing with actual physical limits on the system 
                # we may get away with skipping this step. But it will be very necessary in the long run.


                #If Condition is up to you
                
                ############     DO NOT MODIFY THIS       #########
                ebot_controller.index += 1
                if ebot_controller.flag == 1 :
                    ebot_controller.index = 0
                ebot_controller.send_request(ebot_controller.index)
                ####################################################

        # Spin once to process callbacks
        rclpy.spin_once(ebot_controller)
    
    # Destroy the node and shut down ROS
    ebot_controller.destroy_node()
    rclpy.shutdown()

    if __name__ == '__main__':
        main()
```
```bash
        x = [4, -4, -4, 4, 0]
        y = [4, 4, -4, -4, 0]
        theta = [0, 0, 0, 0, 0]
        # the following theta desired are optional since throughout hologlyph theme we shall set theta_desired or theta_goals to 0. 
        # theta = [0, PI/2, PI, -PI/2, 0]
```
  ## Control Loop!
```bash
    while rclpy.ok():

        # Find error (in x, y and theta) in global frame
        # the /odom topic is giving pose of the robot in global frame
        # the desired pose is declared above and defined by you in global frame
        # therefore calculate error in global frame

        # (Calculate error in body frame)
        # But for Controller outputs robot velocity in robot_body frame, 
        # i.e. velocity are define is in x, y of the robot frame, 
        # Notice: the direction of z axis says the same in global and body frame
        # therefore the errors will have have to be calculated in body frame.
        # 
        # This is probably the crux of Task 1, figure this out and rest should be fine.

        # Finally implement a P controller 
        # to react to the error with velocities in x, y and theta.

        # Safety Check
        # make sure the velocities are within a range.
        # for now since we are in a simulator and we are not dealing with actual physical limits on the system 
        # we may get away with skipping this step. But it will be very necessary in the long run.

        rclpy.spin_once(ebot_controller)

    ebot_controller.destroy_node()
    rclpy.shutdown()
```
The content of the comment in above code very import so let’s repeat it here:

Find error (in x, y and theta) in global frame

the /odom topic is giving present pose of the robot in global frame
the desired pose is declared above and defined by you in global frame therefore calculate error in global frame
Calculate error in body frame

Controller outputs robot velocity in robot_body frame, i.e. velocity are define is in x, y of the robot frame,
Notice: the direction of z axis says the same in global and body frame therefore the errors will have have to be calculated in body frame.
Finally implement P controllers to react to the error in robot_body frame with velocities in x, y and theta in robot_body frame: [v_x, v_y, w]Thats it!

If the robot goes to the desired goal pose (defined by you), Congratulations! You have achieved a major milestone!

Now it’s time to extend (add some logic) the above code to handle a sequence of desired poses.

So now [x_d, y_d, theta_d] instead of being single values we shall have a list of desired goal poses.
```bash
# Example
self.x_goals = [1, -1, -1, 1, 0]
self.y_goals = [1, 1, -1, -1, 0]
self.theta_goals = [0, 0, 0, 0, 0]
```
Once you have entered a list of goal poses, make necessary changes to the control loop to:

go-to-goal-pose of a certain index (index = 0 at start)
identify if the goal has been reached (write an if condition)
stabilise/stay at the goal pose for at least 1 second
increment index if index < length of the list.
repeat
