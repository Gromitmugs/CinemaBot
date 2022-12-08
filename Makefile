.PHONY: remote-launch

remote-launch:
	roslaunch cinema_bot cinema_bot_local_launch.launch

.PHONY: local-bringup-launch

local-bringup-launch:
	echo initiating camera_node
	rosrun cinema_bot camera_node.py

	echo performing bringup
	roslaunch turtlebot3_bringup turtlebot3_robot.launch