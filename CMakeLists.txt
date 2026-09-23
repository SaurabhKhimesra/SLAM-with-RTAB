cmake_minimum_required(VERSION 3.8)
project(isaac_sim_mobile_robot_rtab_map)

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # This package ships launch files and a USD stage, no source files carrying
  # copyright headers, so skip the copyright linter.
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
