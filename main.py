import cv2
import numpy as np
import mediapipe as mp
import time
import autopy
cap= cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
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
                    print(x,y)

    # print(hands)
    cv2.imshow("Image",image)
    cv2.waitKey(1)