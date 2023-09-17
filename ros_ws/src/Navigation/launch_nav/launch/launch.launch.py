from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    check = Node(
        package="gps_distance",
        executable="completeSoftwareOnboarding",
    )

    ld.add_action(check)

    return ld