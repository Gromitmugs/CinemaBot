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
    "0": Customer("GoHome"),
    "1" : Customer('Jedi'),
    "2": Customer('Eisen'),
    "3": Customer('Pooh')
}   

seatDict = {
    "0": Seat('Home', Pose(Point(0.21366995573043823,-0.6690627336502075,0), Quaternion(0,0,0.9934667750568802,0.11412171948442727))),
    "1": Seat('A0', Pose(Point(-0.8531849384307861,0.6736287474632263,0), Quaternion(0,0,-0.755657174205176,  0.6549673542034353))),
    "2": Seat('A1', Pose(Point(0.05283825099468231,0.4579390585422516,0), Quaternion(0,0,0.6406911450212938,0.7677987084459725))),
    "3": Seat('A2', Pose(Point(1.0644069910049438,0.26370003819465637,0), Quaternion(0,0,0.6311260286247685, 0.7756803052755226)))

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
