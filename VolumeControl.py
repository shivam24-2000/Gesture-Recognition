import cv2
import mediapipe as mp
from handTrackingmodule import handDetect

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)


Detector = handDetect()


capture = cv2.VideoCapture(0)

while True:
    success, img = capture.read()

    lmlist, img = Detector.lmlist(img)

    if lmlist:
        length, img = Detector.findDis(4,8,img, lmlist, True)
        print(length)

    







    cv2.imshow("hands", img)
    key = cv2.waitKey(1)

    if(key == 27):
        break

capture.release()
cv2.destroyAllWindows
