# Software-Team-Entrance-Task

## Pre-requisites

Make sure that you have gone through the following repository before starting this task:
[Software Dev guide](https://github.com/YorkURobotics/yurs-rover-software-dev-guide)

## Task Overview

The goal of this task is to create a simple ROS node that recives the current gps location and calculates the distance and the heading between the current location and multiple target locations. Once these distances and headings are calculated, you must publish them to their respective topics with a custom message that meets our testing criteria.

## Workpalce Structure

Within the `ros_ws/src` directory, we store all of our ros packages grouped by their respective subsystem. Our current setup has the following subsystems and packages:

- `navigation` - Contains all of the packages related to the localization of the rover
  -- `launch_nav` - Contains the launch file that is used to launch all of the nodes related to navigation
  -- `gps` - Contains the node that is used to get the current gps location of the rover (will not be used for this task as it needs a gps module to work, insteadf you will be using `testing/test_gps` to simulate the gps node)

- `testing` - Contains all of the packages related to testing different nodes of the rover
  -- `launch_test` - Contains the launch file that is used to launch all of the nodes related to testing
  -- `test_gps` - Contains the node that will be used to test the node created for this task

- `interfaces` - Contains all of the custom messages, services,and actions that are used within our workspace.
  -- `msg` - Contains all of the custom messages that are used within our workspace.
  -- `srv` - Contains all of the custom services that are used within our workspace.
  -- `action` - Contains all of the custom actions that are used within our workspace.
