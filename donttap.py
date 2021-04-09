# Gafencu Gabriel
# donttap.com clicker - currently works only on chrome with a 1920x1080 res.

import numpy as np
import pyautogui
import imutils
import cv2

while True:
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    left_x = 630
    left_y = 230
    width = 620
    height = 630

    image = image[left_y:left_y + height, left_x:left_x + width]

    kernel = np.ones((5, 5), np.uint8)
    image = cv2.dilate(image, kernel)

    ret, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY_INV)

    cnts = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        c = cnts[0]
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        pyautogui.click(x=left_x + cX, y=left_y + cY)

    cv2.imshow("Screenshot", image)
    cv2.waitKey(1)
