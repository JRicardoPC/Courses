cmake_minimum_required(VERSION 2.8.3)
project(robotic)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  visualization_msgs
  tf
  tf2
  tf2_ros
)

## Generate messages in the 'msg' folder
add_message_files(
   FILES
   TwoInts.msg
)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
# )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime visualization_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#This will create executables of the nodes
add_executable(Marker_publisher src/marker_publisher.cpp)


#This will generate message header file before building the target
add_dependencies(Marker_publisher robotic_generate_messages_cpp)


#This will link executables to the appropriate libraries
target_link_libraries(Marker_publisher ${catkin_LIBRARIES})


