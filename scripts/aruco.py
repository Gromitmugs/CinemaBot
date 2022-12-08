import sys

import cv2
import cv2.aruco as aruco
import numpy as np


class ArUco:
    def detectArucoID(frame, marker_size=6, total_markers=250):

        arucoType = f"DICT_{marker_size}X{marker_size}_{total_markers}"

        # define names of each possible ArUCo tag OpenCV supports
        ARUCO_DICT = {
            "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
            "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
            "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
            "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
            "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
            "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
            "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
            "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
            "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
            "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
            "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
            "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
            "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
            "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
            "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
            "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
            "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
            "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
            "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
            "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
            "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
        }

        # check if the input ArUCo tag exists and supported by openCV
        if arucoType not in ARUCO_DICT:
            print(f"[INFO] ArUCo tag of {arucoType} is not supported")
            sys.exit()

        # load the ArUCo dictionary and grab the ArUCo parameters
        arucoDict = aruco.Dictionary_get(ARUCO_DICT[arucoType])
        arucoParams = aruco.DetectorParameters_create()

        # detect ArUCo markers in the input frame
        _, ids, _ = aruco.detectMarkers(
            frame, arucoDict, parameters=arucoParams)

        if ids == None:
            return None
        return ids[0][0]
