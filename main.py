import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5,maxHands=2)
cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,400)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1) # Right Hand will be the left hand and Left hand will be the right hand
    hand, img = detector.findHands(img)
    if hand and hand[0]["type"] == "Left": # If there is a hand and if the hand is Right ie Left after flipped
        fingers = detector.fingersUp(hand[0]) # It will return array of 5 numbers
        totalFingers = fingers.count(1) # Here 1 will count no. of fingers which are open and 0 will count no. of fingers which are close
        cv2.putText(img,f"Fingers: {totalFingers}",(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        # If all fingers are 5 then press 'Right' key and release 'Left' key
        if totalFingers == 5:
            pyautogui.keyDown("right")
            pyautogui.keyUp("left")
        # If all fingers are 0 then press 'Left' key and release 'Right' key
        if totalFingers == 0:
            pyautogui.keyDown("left")
            pyautogui.keyUp("right")
            
    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)