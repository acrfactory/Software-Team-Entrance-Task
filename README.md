# Software-Team-Entrance-Task

## Pre-requisites

Make sure that you have gone through the following repository before starting this task:
[Software Dev guide](https://github.com/YorkURobotics/yurs-rover-software-dev-guide)

## Task Overview

<!--The goal of this task is to create a simple ROS2 node that receives the current GPS location and calculates the distance and the heading between the current location and multiple target locations. Once these distances and headings are calculated, you must publish them to their respective topics with a custom message that meets our testing criteria.-->
To effectively operate our rover in the field, it's crucial to have the ability to calculate the distance and heading to objects of interest relative to the rover. This information is valuable for many applications such as aligning radio equipment and autonomous traversal. The responsibility of acquiring and publishing this information has fallen to you. Your task is to create a ROS2 node that performs this calculation and provides real-time updates to the rover's control system. Below you will find a breakdown of the key components, requirements, and steps involved.

## Workplace Structure

Within the `ros_ws/src` directory, we store all of our ros packages grouped by their respective subsystem. Our current setup has the following subsystems and packages:

- `Navigation` - Contains all of the packages related to the localization of the rover

  - `launch_nav` - Contains the launch file that is used to launch all of the nodes related to navigation
  - `GPS` - Contains the node that is used to get the current GPS location of the rover (will not be used for this task as it needs a GPS module to work, instead you will be using `testing/test_gps` to simulate the GPS node)
  - `gps_distance` - **You must make this package**

- `testing` - Contains all of the packages related to testing different nodes of the rover

  - `launch_test` - Contains the launch file that is used to launch all of the nodes related to testing
  - `test_gps` - Contains the node that will be used to test the node created for this task

- `interfaces` - Contains all of the custom messages, services, and actions that are used within our workspace.
  - `msg` - Contains all of the custom messages that are used within our workspace.
  - `srv` - Contains all of the custom services that are used within our workspace.
  - `action` - Contains all of the custom actions that are used within our workspace.

## Requirements

- Must use Ros2 Humble
- Must be running on an Ubuntu 22.04 environment (can be a VM or WSL)
- The ros2 node can be created in Python or C++.
- Node must be added to the main launch file of the navigation subsystem (does need to be run for this task).
- You need to make a launch file within the `ros_ws/src/testing/launch_test/launch` directory. The launch file should be named `nav_test.launch.py`. The launch file should launch the `test_gps` node and the node created for this task.
- The node created for this task should publish the distance and heading to a custom topic. The node should also subscribe to a topic that publishes the current GPS location in the form of a NavSatFix message.
- Must use Git in order to fork repo (must be a private fork as your solution should not be public) and create a separate branch to work on, once you are done, you must create a pull request to the main branch on the forked repo.

## Task Breakdown

### 1. Creating a ros package

The first step you must take is to create a new ros package within the `ros_ws/src/navigation` directory where all packages related to navigation are housed. This package should be named `gps_distance`.

### 2. Subscribing to current GPS location

The node should publish the distance and heading to a custom topic. The node should also subscribe to the `/current_gps` topic that publishes the current GPS location in the form of a [`NavSatFix` message](https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/NavSatFix.html).

### 3. Calculating distance and heading

The ros parameters indicate the ID of the target locations that the rover must travel to. Once the ID of the target location is known, the node can use the following formula to calculate the distance and heading between the current location and the target location:

![Distance and Heading Formula](

)

**Note:** The heading should be relative to true north in a clockwise direction in degrees and the distance should be in meters.

### 4. Publishing distance and heading (with custom message)

You must publish the distance and heading to a custom topic with a custom message. The custom message must have the following fields:

- an integer (unsigned of size 8 bits) with the variable name `id` representing the id of the target location
- a float (signed of size 32 bits) with the variable name `distance` representing the distance between the current location and the target location in meters
- a float (unsigned of size 32 bits) with the variable name `heading` representing the heading between the current location and the target location in degrees relative to true north in a clockwise direction

### 5. Creating a launch file

Now that you have created the node, you must create a launch file that will launch the node. The launch file should be named `nav_test.launch.py` and should be placed within the `ros_ws/src/testing/launch_test/launch` directory. The launch file should launch the `test_gps` node and the node created for this task.

The parameters for the `test_gps` node should be the last 3 digits of your student number. For example, if your student number is 123456789, the parameters should be 789, which means that the three location ids that the rover must travel to are 7, 8, and 9.

Launching this launch file should result in output that looks like the following:

```bash
[INFO] [launch]: All log files can be found below /home/rover/.ros/log/2021-09-30-16-00-00-000000-rover-0
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [test_gps-1]: process started with pid [42069]
[INFO] [gps_distance-2]: process started with pid [69420]
[INFO] [test_gps-1]: Publishing current GPS location: 43.945, -78.895
[INFO] [test_gps-1]: Received CORRECT distance and heading to target location 7: 100.0m, 45.0 degrees
[INFO] [test_gps-1]: Received CORRECT distance and heading to target location 8: 200.0m, 90.0 degrees
[INFO] [test_gps-1]: Received INCORRECT distance and heading to target location 9: 300.0m, 135.0 degrees
```

If all of the Logs are correct, then you have completed the task. If not, then you must go back and fix the errors.

## Submission

Once you have completed the task, you must submit your solution to the task by filling out the following form:
[YURS Software Entrance Task Submission](https://forms.gle/)

### Deliverables

- A link to the forked private repo that contains your solution to the task (must be shared with @karanpreet_raja for evaluation), the repo should contain the following:
  - A ros package named `gps_distance` within the `ros_ws/src/navigation` directory
  - A node within the `gps_distance` package that publishes the distance and heading to a custom topic. The node should also subscribe to a topic that publishes the current GPS location in the form of a NavSatFix message.
  - Create a launch file named `nav_test.launch.py` within the `ros_ws/src/testing/launch_test/launch` directory. The launch file should launch the `test_gps` node and the node created for this task.
  - Add the node created for this task to the main launch file of the navigation subsystem which is located at `ros_ws/src/navigation/launch_nav/launch/navigation.launch.py` (does need to be run for this task).
- A video of the output of the launch file created for this task. The video should show the output of the launch file and the terminal where the launch file was run.
