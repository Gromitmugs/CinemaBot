#!/usr/bin/env python3

import playsound
import rospy
from std_msgs.msg import String


def voice_node(): # node name
    print("Voice Node Active")
    sub = rospy.Subscriber('/PlaySound', String, callback)
    rospy.init_node('voice_node')
    rate = rospy.Rate(10) # 10hz
    rospy.spin()

def callback(data):
    if data.data == "Going Home":
        playsound.playsound('/home/eisen/catkin_ws/src/cinema_bot/mp3s/thank_you_enjoy.mp3', True)
    else:
        playsound.playsound('/home/eisen/catkin_ws/src/cinema_bot/mp3s/please_follow_me.mp3', True)

if __name__ == "__main__":
    try:
        voice_node()
    except rospy.ROSInterruptException:
        pass
