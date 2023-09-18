# Software-Team-Entrance-Task

## Pre-requisites

Make sure that you have gone through the following repository before starting this task:
[Software Dev guide](https://github.com/YorkURobotics/yurs-rover-software-dev-guide)

## Task Overview

<!--This task aims to create a simple ROS2 node that receives the current GPS location and calculates the distance and heading between the current location and multiple target locations. Once these distances and headings are calculated, you must publish them to their respective topics with a custom message that meets our testing criteria.-->
To effectively operate our rover in the field, it's crucial to have the ability to calculate the distance and heading to objects of interest relative to the rover. This information is valuable for many applications such as aligning radio equipment and autonomous traversal. The responsibility of acquiring and publishing this information has fallen to you. Your task is to create a ROS2 node that performs this calculation and provides real-time updates to the rover's control system. Below you will find a breakdown of the critical components, requirements, and steps involved.

## Workplace Structure

Within the `ros_ws/src` directory, we store all of our ros packages grouped by their respective subsystem. The workspace for this task has the following subsystems and packages:

- `Navigation` - Contains all of the packages related to the localization of the rover

  - `launch_nav` - Contains the launch file that is used to launch all of the nodes related to navigation
  - `GPS` - Contains the node that is used to get the current GPS location of the rover (will not be used for this task as it needs a GPS module to work, instead you will be using `testing/test_gps` to simulate the GPS node)
  - `gps_distance` - **You must make this package**

- `testing` - Contains all of the packages related to testing different nodes of the rover

  - `launch_test` - Contains the launch file that is used to launch all of the nodes related to testing
  - `test_gps` - Contains the node that will be used to test the node created for this task

- `interfaces` - Contains all of the custom messages, services, and actions that are used within our workspace.
  - `msg` - Contains all of the custom messages that are used within our workspace.

## Requirements

- Must use Ros2 Humble
- Must be running on an Ubuntu 22.04 environment (can be a VM or WSL)
- Your ros2 node can be created in Python or C++.
- Your node must be added to the main launch file of the navigation subsystem (although you may launch your package using ```bash ros2 run ```.
- Must use Git to fork the repository (you must make a private fork as your solution should not be public), and create a separate branch to work on, once you are done, you must create a pull request to the main branch on the forked repository.

## Task Breakdown

### 1. Creating a ros package

Firstly create a new ros package within the `ros_ws/src/Navigation` directory, this package should be named `gps_distance`.

### 2. Subscribing to current GPS location

Your node will receive [NavSatFix]([url](https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/NavSatFix.html)) messages over the "GCS" topic, only the latitude and longitude fields are populated. You may gain some insight into the structure of the message by running ```bash ros2 topic echo "GCS"``` after the launch_test script has been launched using ```bash ros2 launch lauch_test launch.launch.py```.

### 3. Calculating distance and heading

The formula you will use for the arithmetic is called the [Haversine]([url](https://en.wikipedia.org/wiki/Haversine_formula)) formula, this formula is used to compute the great-circle distance between two points on a sphere. You are not allowed to use an existing Python package to do this calculation for you. An important consideration for the distance calculation is that the earth is not a perfect sphere, for this task, it will be assumed that we are operating at CIRC Summer which is held in Drumheller Alberta. The radius of the earth at the operating site should be assumed to be 6365.766km. This radius is the sum of the altitude and radius for a given latitude.



### 4. Publishing distance and heading (with custom message)

Your output should be published to the “Dish” topic for every pair of GCS coordinates individually as they are received.
The format of your custom message must meet the message specifications exactly, otherwise, your work will not be able to be checked by the check node. The message should consist of four float64 fields named as follows “latitude”, “longitude”, “distance”, and “heading”. Where the “latitude” and “longitude” are the GCS coordinate pair of the rover received on the topic “GCS”, “distance” is the distance in meters rounded to one decimal point between the received rover GCS pair and the fixed dish coordinates (51.42287924341543,-112.64106837507106). “Heading” is the heading of the dish from the rover, this heading is measured in degrees off of true north rounded to one decimal point (once you have implemented the Haversine formula for calculating distance, it should become more obvious on how heading should be computed)

<!-- Instructions for adding a custom message-->


### 5. Adding your node to the launch file
<!-- as it is right now this launch file already exists-->

Now that you have created the node, you must add it to the Navigation packages launch file. The launch file should be named `nav_test.launch.py` and should be placed within the `ros_ws/src/Navigation/launch` directory. The launch file should launch the node you created for this task.

### 6. Testing

In order to test your node, you must launch both your launch file and the launch_test file. These should be launched in separate terminals.

```bash ros2 launch launch_test launch.launch.py```
```bash ros2 launch {yourlauchpackage} {yourlaunchfile}```

You should receive feedback in the terminal you ran launch_test in. This feedback is limited to message issues 

## Submission

Once you have completed the task, you must submit your solution to the task by filling out the following form:
[YURS Software Entrance Task Submission](https://forms.gle/Haa34G6QinaqzdEi7)

### Deliverables

- A link to the forked private repo that contains your solution to the task (must be shared with @karanpreet_raja for evaluation), the repo should contain the following:
  - A ros package named `gps_distance` within the `ros_ws/src/navigation` directory
  - A node within the `gps_distance` package that publishes the distance and heading to a custom topic. The node should also subscribe to a topic that publishes the current GPS location in the form of a NavSatFix message.
  - Create a launch file named `nav_test.launch.py` within the `ros_ws/src/Navigation/launch` directory. <!-- specific naming optionally -->
- A video of the output of the launch file created for this task. The video should show the output of the launch file and the terminal where the launch file was run.
