import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()     

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
 
    lower_blue = np.array([100,100,120]) 
    upper_blue = np.array([150,255,255]) 
    lower_green = np.array([50, 150, 50]) 
    upper_green = np.array([80, 255, 255]) 
    lower_red = np.array([150, 50, 50])
    upper_red = np.array([180, 255, 255]) 
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.inRange(hsv, lower_green, upper_green) 
    mask2 = cv2.inRange(hsv, lower_red, upper_red) 
     
    res = cv2.bitwise_and(frame, frame, mask=mask) 
    res1 = cv2.bitwise_and(frame, frame, mask=mask1) 
    res2 = cv2.bitwise_and(frame, frame, mask=mask2) 

    cv2.imshow('original',frame) 
    cv2.imshow('Blue', res) 
    cv2.imshow('Green', res1) 
    cv2.imshow('red', res2) 
    if cv2.waitKey(1) == ord('q'): 
        break

capture.release()                  
cv2.destroyAllWindows()            