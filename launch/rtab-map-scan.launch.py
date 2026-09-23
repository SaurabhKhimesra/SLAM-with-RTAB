import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def find_launch_file(package, filename):
    """Look up a launch file anywhere under a package's share/launch tree.

    rtabmap_demos moved its demos into per-robot subfolders (turtlebot3/,
    husky/, ...) in December 2024, so the file sits at launch/turtlebot3/ on
    newer installs and at launch/ on older ones. Searching handles both.
    """
    launch_dir = os.path.join(get_package_share_directory(package), 'launch')
    for root, _, files in os.walk(launch_dir):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(
        '{} not found under {} - is {} installed?'.format(filename, launch_dir, package))


def generate_launch_description():
    """Run RTAB-Map 2D scan SLAM against the Isaac Sim lidar."""
    use_sim_time = LaunchConfiguration('use_sim_time')

    turtlebot3_scan_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            find_launch_file('rtabmap_demos', 'turtlebot3_scan.launch.py')),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use the /clock topic published by Isaac Sim',
        ),
        turtlebot3_scan_launch,
    ])
