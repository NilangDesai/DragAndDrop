import cv2
from HandTrackingModule import HandDetector
cap=cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
detector=HandDetector(detectionCon=0.5)
cx,cy,w,h=100,100,200,200
color=(255,0,255)


class DragRect():
    def __init__(self,poscenter,size=[200,200]):
        self.poscenter=poscenter
        #print(self.poscenter)
        self.size=size

    def update(self,cursor):
        cx,cy=self.poscenter
        w,h=self.size

        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.poscenter= cursor

rectList=[]
for x in range(5):
    rectList.append(DragRect([x*250+150,150]))



while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    img=detector.findhands(img)
    lmList,_=detector.findposition(img,draw=False)
    #print(lmList)
    if lmList:
        l,_=detector.finddistance(img,8,12,draw=False)
        #print(l)
        if l<50:
            cursor=lmList[8]
            for rect in rectList:
                rect.update(cursor)




    for rect in rectList:
        cx,cy=rect.poscenter
        w,h=rect.size
        cv2.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),color,cv2.FILLED)



    cv2.imshow("img",img)
    cv2.waitKey(1)
