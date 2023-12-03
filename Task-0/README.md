## Task 0

## 1. Installation of Ubuntu and ROS 2 🛠
In order to successfully complete all the tasks in this eYRC Theme you need to install the following.

## 1. Ubuntu 22.04.3 LTS (https://ubuntu.com/download/desktop/thank-you?version=22.04.3&architecture=amd64)

![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/f73a02a5-562a-4ebc-be22-d12f5782d689)

Important Note

We highly recommend participants to NOT use Virtual Machine as setup for this theme. (No support will be provided from eyantra,if you are using a virtual machine)

Participants should only install Ubuntu version 22.04.3 LTS (Jammy jellyfish).

Since in HB Theme, ROS2 Humble distribution is used which is compatible only with Ubuntu 22.04.3 LTS

## Installation Guide of Ubuntu 22.04:
https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview

![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/7858f124-6969-4eab-93d4-8040903d7bba)

## 2. ROS2 Humble Installation: humble

![image](https://github.com/pooja8748/Hologlyph-Bots-/assets/130728514/6376274e-27cb-456b-ba7d-25d6c167a617)

ROS2:
Robot Operating System (ROS) is a set of software libraries and tools for building robot applications. From drivers and state-of-the-art algorithms to powerful developer tools, ROS has the open source tools you need for your next robotics project.

Since ROS was started in 2007, a lot has changed in the robotics and ROS community. The goal of the ROS 2 project is to adapt to these changes, leveraging what is great about ROS 1 and improving what isn’t.

First thing after installing a fresh Ubuntu is upgrading your system to the latest one, to do that, open a terminal (press Ctrl+Alt+t) on your keyboard and copy the below 👇 commands carefully and press enter to execute a command.


```bash

 sudo apt upgrade

```

Set locale
Make sure you have a locale which supports UTF-8.
If you are in a minimal environment (such as a docker container), the locale may be something minimal like POSIX.
We test with the following settings. However, it should be fine if you’re using a different UTF-8 supported locale.

```bash

 locale  # check for UTF-8

 sudo apt update && sudo apt install locales
 sudo locale-gen en_US en_US.UTF-8
 sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
 export LANG=en_US.UTF-8

 locale  # verify settings

```
Setup Sources
You will need to add the ROS 2 apt repository to your system.

```bash

 sudo apt install software-properties-common
 sudo add-apt-repository universe

```
Now add the ROS 2 GPG key with apt.

```bash

 sudo apt update && sudo apt install curl -y
 sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

```
Then add the repository to your sources list.

```bash

 echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

```

Install ROS 2 packages

Update your apt repository caches after setting up the repositories.

```bash

 sudo apt update

```
ROS Desktop Install

```bash

 sudo apt install ros-humble-desktop

```
Note: Desktop installation is recommended because the software utilized in this theme can only be used with Desktop.

## Environment setup
To Automatically add ROS environment variables to your bash session every time a new shell terminal/bash is launched, enter the following commands (this step is similar as adding environmental variable in windows)
(Find more about bash)

```bash

 echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

```
## 3. Gazebo Installation: gazebo

To install gazebo please copy the below👇 command

```bash

  sudo apt install ros-humble-gazebo-ros
  sudo apt install ros-humble-gazebo-plugins

```


