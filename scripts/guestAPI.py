#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point, Pose, Quaternion

from cinema_bot.srv import GuestAPI, GuestAPIResponse


class Customer:
    def __init__(self, n):
        self.name = n

class Seat:
    def __init__(self, n, pose):
        self.number = n
        self.location = pose

guestDict = {
    "0" : Customer('Jedi'),
    "1": Customer('Eisen'),
    "2": Customer('Pooh')
}   

seatDict = {
    "0": Seat('A0', Pose(Point(0,0,0), Quaternion(0,0,0,0)))
}

def guest_api_server():
    rospy.init_node('guest_api_server')
    s = rospy.Service('guest_api', GuestAPI, handle_guest_api)
    print("Guest API running")
    rospy.spin()
    
def handle_guest_api(request):
    global guestDict
    global locationDict
    print('Hello ' + guestDict[request.arucoId].name)
    print('Your seat number is '+ seatDict[request.arucoId].number)
    return GuestAPIResponse(seatDict[request.arucoId].location, guestDict[request.arucoId].name)

if __name__ == "__main__":
    guest_api_server()
