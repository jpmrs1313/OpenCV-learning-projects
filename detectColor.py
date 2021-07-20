import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max", "TrackBars",179,179,empty)
cv2.createTrackbar("Saturation Min", "TrackBars",0,255,empty)
cv2.createTrackbar("Saturation Max", "TrackBars",255,255,empty)
cv2.createTrackbar("Value Min", "TrackBars",0,255,empty)
cv2.createTrackbar("Value Max", "TrackBars",255,255,empty)

path=r"C:\Users\jpmrs\OneDrive\Desktop\laranja.jpg"
while True:
    success, img = cap.read()

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min","TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max","TrackBars")
    v_min = cv2.getTrackbarPos("Value Min","TrackBars")
    v_max = cv2.getTrackbarPos("Value Max","TrackBars")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)


    cv2.imshow("Mask",mask)
    cv2.waitKey(1)