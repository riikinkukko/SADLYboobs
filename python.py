import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def yellow(hsv, image):
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_yellow:
        x, y, w, h = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Центр объекта: ({}, {})".format(center_x, center_y))

    cv2.imshow('Result', image)
def red(hsv, image):
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_red:
        x, y, w, h = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Центр объекта: ({}, {})".format(center_x, center_y))

    cv2.imshow('Result', image)
while True:
    _, image = cap.read()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    yellow(hsv, image)
    red(hsv, image)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
