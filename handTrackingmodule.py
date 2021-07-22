import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw_tool = mp.solutions.drawing_utils

class handDetect():
    def lmlist(self, img, draw = True):
        lmlist = []
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        if(result.multi_hand_landmarks):
            for handlms in result.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    h,w,c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lmlist.append([id,cx,cy])
            if draw:
                draw_tool.draw_landmarks(img, handlms, mp_hands.HAND_CONNECTIONS)

        return lmlist, img

    def fingersUp(self, img, lmlist, draw = True):
        fingers = []
        tipsid = [8,12,16,20]
        count = 0;
        if(lmlist[4][1] < lmlist[3][1]):
            fingers.append(0)
        else:
            fingers.append(1)
            count += 1

        for id in tipsid:
            if(lmlist[id][2] < lmlist[id - 2][2]):
                fingers.append(1)
                count += 1
            else:
                fingers.append(0)
        if draw:
            cv2.putText(img, str(count), (50,100), cv2.FONT_HERSHEY_COMPLEX, 3,(255,0,255), 3)

        return fingers, img

    def findDis(self, p1, p2 ,img, lmlist, draw=False):
        x1, y1 = lmlist[p1][1:]
        x2, y2 = lmlist[p2][1:]

        length = math.hypot(x2-x1, y2-y1)

        if draw:
            cv2.line(img, (x1,y1),(x2,y2), (255,0,255),3)

        return length, img


