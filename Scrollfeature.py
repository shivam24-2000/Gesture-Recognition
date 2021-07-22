import cv2
import mediapipe as mp
from handTrackingmodule import handDetect
import pyautogui as py

Detector = handDetect()



capture = cv2.VideoCapture(0)

while True:
    success, img = capture.read()

    lmlist, img = Detector.lmlist(img)

    if lmlist:
        fingers, img = Detector.fingersUp(img, lmlist)

        if(fingers == [0,0,0,0,0]):
            py.scroll(-50)
        elif(fingers == [1,1,1,1,1]):
            py.scroll(50)


        # print(fingers)

    







    cv2.imshow("hands", img)
    key = cv2.waitKey(1)

    if(key == 27):
        break

capture.release()
cv2.destroyAllWindows
