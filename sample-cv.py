# Finding rectangles

import cv2
import numpy as np
import math

MaxDiagonal = 200
MinDiagonal = 50

def GetRectAngles (gray):

    contours = 0
    thresh = 0
    rectangles = list()
    count = 0

    _,thresh = cv2.threshold(gray,65,255,0)
    _, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        xy,wh,angle = rect
        w,h = np.int0(wh)

        if ((w*w + h*h)**0.5 > MinDiagonal) & ((w*w + h*h)**0.5 < MaxDiagonal):
            count = count + 1
            rectangles.append(rect)
            cv2.drawContours(gray,[box],0,(10,20,255),2)
            x,y = np.int0(xy)
            if w>h :
                x1 = np.int0(x+w)
                y1 = np.int0(y+w*math.tan(math.radians(angle)))
                cv2.arrowedLine(gray,(x,y),(x1,y1),(255,255,255))
            else :
                x1 = np.int0(x+w)
                y1 = np.int0(y+w*math.tan(math.radians(angle+90)))
                cv2.arrowedLine(gray,(x,y),(x1,y1),(255,255,255))

    cv2.imshow('ShowFoundRects', gray)
    print count,' rectangles found. Press ESC to exit'
    return rectangles


cap = cv2.VideoCapture(0)

while 1:

    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    RectAngles = GetRectAngles(gray)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
