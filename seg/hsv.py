import feature
import numpy as np
import cv2
from matplotlib import pyplot as plt
def hsv(file):
    img = cv2.imread(file + ".jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    a = (1, 190, 200)
    sum = (18, 255, 255)
    mask = cv2.inRange(hsv, a, sum)
    edged = cv2.Canny(mask, 10, 250)
    im2, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # _, contours, _= cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        #print(str(w) + " " + str(h))
        if w > 50 and h > 50:
            idx += 1
            new_img = img[y:y + h, x:x + w]
            cv2.imwrite("./hsv/" + file + str(idx) + '.jpg', new_img)
            #print("./hsv/" + file + str(idx))
            feature.feature("./hsv/" + file + str(idx), 0)
#hsv("fruit")