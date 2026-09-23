"""
Open this project's stage in Isaac Sim and step it with the ROS 2 bridge live.

Run with Isaac Sim's own interpreter, from anywhere:

    ./python.sh /path/to/SLAM-with-RTAB/script/run-sim.py
    ./python.sh /path/to/SLAM-with-RTAB/script/run-sim.py /some/other/stage.usd
"""
import os
import sys

from omni.isaac.kit import SimulationApp

# SimulationApp has to be constructed before any other omni.isaac import.
simulation_app = SimulationApp({"headless": False})

from omni.isaac.core import World  # noqa: E402
from omni.isaac.core.utils.stage import open_stage  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_STAGE = os.path.join(REPO_ROOT, "isaac-sim", "ros2-turtlebot.usd")

usd_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_STAGE
if not os.path.isfile(usd_path):
    simulation_app.close()
    raise SystemExit("stage not found: {}".format(usd_path))

open_stage(usd_path=usd_path)

world = World()
world.reset()

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
