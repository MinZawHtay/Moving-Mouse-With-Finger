import cv2
import numpy as np
import mediapipe as mp
import time
import pyautogui
index_y = 0
cap= cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_w,screen_h = pyautogui.size()
while True:
    success, image = cap.read()
    image = cv2.flip(image,1)
    frame_h,frame_w,success = image.shape
    rgb_frame= cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    output =hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)
            landmarks = hand.landmark
            for id , landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    if id == 8:
                         cv2.circle(img=image,center=(x,y),radius=20,color=(255,0,255))
                         index_x =screen_w / frame_w * x
                         index_y = screen_h / frame_h * y
                         pyautogui.moveTo(index_x,index_y)
                    if id == 4:
                         cv2.circle(img=image,center=(x,y),radius=20,color=(255,0,255))
                         thumb_x =screen_w / frame_w * x
                         thumb_y = screen_h / frame_h * y
                         print("Outside",abs(index_y - thumb_y))
                         if abs(index_y - thumb_y) < 20:
                              pyautogui.click()
                              pyautogui.sleep(1)
    # print(hands)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
