cmake_minimum_required(VERSION 3.5)
project(turtlebot_calibration)

install(
  PROGRAMS
  ${PROJECT_NAME}/calibrate.py
  ${PROJECT_NAME}/scan_to_angle.py
  DESTINATION bin
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
