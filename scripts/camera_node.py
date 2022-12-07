#!/usr/bin/env python3

import cv2
import rospy
from aruco import ArUco
from geometry_msgs.msg import Pose

from cinema_bot.srv import GuestAPI


def camera_node(): # node name
    pub = rospy.Publisher('/SeatLocation', Pose, queue_size=10)
    rospy.init_node('camera_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    cap = cv2.VideoCapture(0)

    print("camera node running")
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        corners, ids = ArUco.detectAruco(
            frame, marker_size=5, total_markers=50)

        if len(ids) > 0: #aruco detected
            pose_response = callGuestAPI(str(ids[0]))
            pub.publish(pose_response)


    cap.release()
    cv2.destroyAllWindows()

def callGuestAPI(id):
    try:
            guestAPI = rospy.ServiceProxy('GuestAPI', GuestAPI)
            response = guestAPI(id)
            return response
    except rospy.ServiceException as e:
            print("GuestAPI call failed: %s"%e)

if __name__ == "main":
    try:
        camera_node()
    except rospy.ROSInterruptException:
        pass