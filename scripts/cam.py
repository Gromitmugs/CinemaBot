#!/usr/bin/env python3

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()