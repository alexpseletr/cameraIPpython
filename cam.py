import cv2
import numpy as np
import time

cap = cv2.VideoCapture("rtsp://192.168.1.1:554/user=admin&password=&channel=1&stream=0.spd")

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    time.sleep(0.25)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
