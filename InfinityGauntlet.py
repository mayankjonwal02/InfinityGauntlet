import cv2
import mediapipe as mp
import pyautogui
import numpy as  np
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
screenwidth,screenheight=pyautogui.size()
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(frame1)
    hands=output.multi_hand_landmarks
    fheight,fwidth,_=frame.shape
    if hands:
        for hand in hands:
            #drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*fwidth)
                y=int(landmark.y*fheight)
                if id==2:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,0),thickness=-1)
                    #drawing_utils.draw_landmarks(frame,landmarks)
                if id==5:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(255,0,255),thickness=-1)
                if id==9:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(255,150,0),thickness=-1)

                if id==13:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,0,255),thickness=-1)

                if id==17:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,167,255),thickness=-1)

                if id==0:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,230,255),thickness=-1)
                if id==4:
                    thumbx=screenwidth/fwidth*x
                    thumby=screenwidth/fwidth*y
                if id==8:
                    indexx=screenwidth/fwidth*x
                    indexy=screenwidth/fwidth*y    
                    if(abs(thumby-indexy)<70):
                        frame= cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
                        


    cv2.imshow("thanos",frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()

