import cv2
import torch
import numpy as np
from tracker import *


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap=cv2.VideoCapture('tvid.mp4')

count=0
tracker = Tracker()
counter=0
area_1=set()
cyl=420
offset=5

b=model.names[2] = 'car'

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', POINTS)

area1=[(225,380),(450,395),(460,370),(260,360)]
while True:
    
    ret,frame=cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,600))
    cv2.line(frame,(75,420),(1000,420),(255,225,255),1)
    results=model(frame)
    list=[]
    #a=results.pandas().xyxy[0]
    #print(a)
    for index,rows in results.pandas().xyxy[0].iterrows():
      x1=int(rows['xmin'])
      y1=int(rows['ymin'])
      x2=int(rows['xmax'])
      y2=int(rows['yamax'])
      d=(row['class'])
      if d==2:
        cv2.rectangle(img,(x1, y1),(x2, y2),(0,0,255),2)
        rectx1,recty1=((x1+x2)/2, (y1+y2)/2)
        rectcenter=int(rectx1),int (rectyl)
        cx=rectcenter [0]
        cy=rectcenter [1]
        cv2.circle(img,(cx, cy),3,(0,255,0),-1)
        cv2.putText (ing, str(b),(x1,yl),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),2)
        if cy<(cyl+offset) and cy>(cyl-offset):
            counter+ 1
            cv2.line(frame,(75,420),(1000,420), (0,255,0),2)
            print(counter)
        
    cv2.putText (img, str(counter), (x2, y2), cv2. FONT_HERSHEY_PLAIN, 2, (255,255,255),2)    
    #cv2.polylines(frame,[np.array(area1,np.int32)],True,(225,0,255),1)
    #print(x2,y2,x3,y3)
    #a1=len(area_1)
    #print(a1)
    cv2.putText(frame,str(a1),(160,420),cv2.FONT_HERSHEY_PLAIN,3,(255,225,0),1)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()

