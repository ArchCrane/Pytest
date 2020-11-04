import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking",0,255,nothing)
cv2.createTrackbar("LS", "Tracking",0,255,nothing)
cv2.createTrackbar("LV", "Tracking",0,255,nothing)
cv2.createTrackbar("HH", "Tracking",255,255,nothing)
cv2.createTrackbar("HS", "Tracking",255,255,nothing)
cv2.createTrackbar("HV", "Tracking",255,255,nothing)
while(1):

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    l_h = cv2.getTrackbarPos("LH", "Tracking")
    h_h = cv2.getTrackbarPos("HH", "Tracking")

    l_s = cv2.getTrackbarPos("LS", "Tracking")
    h_s = cv2.getTrackbarPos("HS", "Tracking")

    l_v = cv2.getTrackbarPos("LV", "Tracking")
    h_v = cv2.getTrackbarPos("HV", "Tracking")

    l_b = np.array([l_h,l_s,l_v])    #thresholding the picture for the color blue
    u_b = np.array([h_h,h_s,h_v])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, l_b, u_b)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()