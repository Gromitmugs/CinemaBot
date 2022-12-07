#!/usr/bin/env python3

import cv2
import rospy
from aruco import ArUco
from geometry_msgs.msg import Pose, Point, Quaternion
from cinema_bot.srv import GuestAPI, GuestAPIResponse


def camera_node(): # node name
    pub = rospy.Publisher('/SeatLocation', Pose, queue_size=10)
    rospy.init_node('camera_node')
    rate = rospy.Rate(10) # 10hz

    cap = cv2.VideoCapture(0)
    
    rospy.set_param('RobotStatus','Free')

    while not rospy.is_shutdown():
        robotStatus = rospy.get_param('RobotStatus','Free')
        ret, frame = cap.read()
        if robotStatus != "Serving":   
            frame = cv2.resize(frame, (1280, 720))
            id = ArUco.detectArucoID(
                frame, marker_size=5, total_markers=50)
            if id == None:
                print("no id")
            else: #aruco detected
                print(id)
                pose_response = callGuestAPI(str(id))
                location_pub = parseDataFromGuestAPIResponseToPose(pose_response.seatLocation)
                print(location_pub)
                rospy.set_param('RobotStatus', 'Serving') #set RobotStatus
                pub.publish(location_pub)
        
        if cv2.waitKey(1) == ord('q'):
            break
        rate.sleep()

def callGuestAPI(id):
    try:
        guestAPI = rospy.ServiceProxy('guest_api', GuestAPI)
        response = guestAPI(id)
        return response
    except rospy.ServiceException as e:
            print("GuestAPI call failed: %s"%e)

def parseDataFromGuestAPIResponseToPose(location):
    return Pose(
        Point(
            location.position.x,
            location.position.y,
            location.position.z
        ),
        Quaternion(
            location.orientation.x,
            location.orientation.y,
            location.orientation.z,
            location.orientation.w
        )
    )

if __name__ == "__main__":
    try:
        camera_node()
    except rospy.ROSInterruptException:
        pass
