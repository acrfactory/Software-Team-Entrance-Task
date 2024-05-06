from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    gps_distance_node = Node(
        package="gps_distance",
        executable="gps_distance"
    )

    ld.add_action(gps_distance_node)
    # ld.add_action(check)
    
    # Your code here

    return ld