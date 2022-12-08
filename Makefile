.PHONY: laptop-launch

laptop-launch:
	roslaunch cinema_bot cinema_bot_laptop_launch.launch

.PHONY: turtle-bringup-launch

turtle-bringup-launch:
	roslaunch cinema_bot cinema_bot_init.launch

.PHONY: map_calibrate

map_calibrate:
	roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$$HOME/map.yaml