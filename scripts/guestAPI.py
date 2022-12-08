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
    "0": Seat('Home', Pose(Point(0.5710810422897339,-1.0623873472213745,0), Quaternion(0,0,0.5001923331873626,0.8659143316867913))),
    "1": Seat('A0', Pose(Point(-0.1955731213092804,1.2890892028808594,0), Quaternion(0,0,0.47226153829649153, 0.8814584728992236))),
    "2": Seat('A1', Pose(Point(0.5209435820579529,0.717159628868103,0), Quaternion(0,0,0.5246004036495134,0.8513485869435431))),
    "3": Seat('A2', Pose(Point(1.405967116355896,-0.02360612154006958,0), Quaternion(0,0,0.49794680218992715, 0.8672075773359141)))

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
