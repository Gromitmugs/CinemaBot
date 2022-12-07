#!/usr/bin/env python3

import cv2
import rospy
from aruco import ArUco
from geometry_msgs.msg import Point, Pose, Quaternion

from cinema_bot.srv import GuestAPI, GuestAPIResponse

def camera_node(): # node name
    pub = rospy.Publisher('/SeatLocation', Pose, queue_size=10)
    rospy.init_node('camera_node')
    rate = rospy.Rate(10) # 10hz

    cap = cv2.VideoCapture(0)
    rospy.set_param('RobotStatus','Free')
    while not rospy.is_shutdown():
        robotStatus = rospy.get_param('RobotStatus','Free')
        _, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))

        if robotStatus == "Free":    
            id = ArUco.detectArucoID(
                frame, marker_size=5, total_markers=50)

            if id == None:
                print("no id")
            else: #aruco detected
                print(id)
                pose_response = callGuestAPI(str(id))
                location_pub = parseDataFromGuestAPIResponseToPose(pose_response.seatLocation)
                rospy.set_param('RobotStatus', 'Serving') #set RobotStatus
                rospy.set_param('RecentID',str(id))
                pub.publish(location_pub)
        
        elif robotStatus == "AtDestination":
            id = ArUco.detectArucoID(
                frame, marker_size=5, total_markers=50)

            if id == None:
                print("await for ID")
            elif str(rospy.get_param("RecentID","-1")) == str(id):
                print("Going Back Home")
                pose_response = callGuestAPI(str(0))
                location_pub = parseDataFromGuestAPIResponseToPose(pose_response.seatLocation)
                rospy.set_param("RobotStatus", "GoHome")
                pub.publish(location_pub)
                
            else:
                print("Invalid ID")


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
