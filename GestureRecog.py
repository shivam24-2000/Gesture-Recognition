import cv2
import mediapipe as mp
from handTrackingmodule import handDetect

Detector = handDetect()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw_tool = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)

while True:
    success, img = capture.read()

    lmlist, img = Detector.lmlist(img)

    print(lmlist)
    







    cv2.imshow("hands", img)
    key = cv2.waitKey(1)

    if(key == 27):
        break

capture.release()
cv2.destroyAllWindows
