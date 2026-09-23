"""RViz2 with the Nav2 displays."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    """Open RViz2 with the Nav2 displays."""
    # nav2_bringup's rviz_launch.py already ships the displays we need
    # (map, TF, costmaps, path). It takes no use_sim_time argument.
    rviz_launch_path = os.path.join(
        get_package_share_directory('nav2_bringup'), 'launch', 'rviz_launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource(rviz_launch_path)),
    ])
