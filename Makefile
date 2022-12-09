.PHONY: laptop-launch

laptop-launch:
	roslaunch cinema_bot cinema_bot_laptop_launch.launch

.PHONY: bringup

bringup:
	roslaunch turtlebot3_bringup turtlebot3_robot.launch

.PHONY: map-calibrate

map_calibrate:
	roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$$HOME/map.yaml

.PHONY: map-creation
map-creation:
	roslaunch turtlebot3_slam turtlebot3_slam.launch

.PHONY: camera-node-init

camera-node-init:
	roslaunch cinema_bot cinema_bot_camera_node.launch

.PHONY: voice-node-init
voice-node-init:
	rosrun cinema_bot voice.py
