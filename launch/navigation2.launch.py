import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    """Bring up the Nav2 stack against the Isaac Sim topics."""
    use_sim_time = LaunchConfiguration('use_sim_time')

    navigation_launch_file = os.path.join(
        get_package_share_directory('nav2_bringup'), 'launch', 'navigation_launch.py')

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(navigation_launch_file),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use the /clock topic published by Isaac Sim',
        ),
        navigation_launch,
    ])
