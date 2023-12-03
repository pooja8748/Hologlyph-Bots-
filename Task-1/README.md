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

![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/42df291e-253e-4e25-989e-8a495cefb3bd)

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
