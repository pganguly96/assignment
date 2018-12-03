import feature
import numpy as np
import cv2
from matplotlib import pyplot as plt

def seg(file):
    img = cv2.imread(file + ".jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    border, thresholdedValue = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # noise removal
    oneArray = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresholdedValue, cv2.MORPH_OPEN, oneArray, iterations=2)
    # sure background area
    bg = cv2.dilate(opening, oneArray, iterations=3)
    # Finding sure foreground area
    distance = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    border, fg = cv2.threshold(distance, 0.7 * distance.max(), 255, 0)
    # Finding bgFg region
    fg = np.uint8(fg)
    bgFg = cv2.subtract(bg, fg)
    # Marker labelling
    border, markers = cv2.connectedComponents(fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of bgFg with zero
    markers[bgFg == 255] = 0
    markers = cv2.watershed(img, markers)
    img1 = img.copy()
    img1[markers == -1] = [255, 255, 255]
    img1[markers != -1] = [0, 0, 0]
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(img1, 10, 250)
    _, contours, _ = cv2.findContours(thresholdedValue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # _, contours, _= cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    #print("deep")
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        #print(str(w) + " " + str(h))
        if w > 25 and h > 25:
            idx += 1
            new_img = img[y:y + h, x:x + w]
            #print("deep")
            cv2.imwrite("./str/" + file + str(idx) + '.jpg', new_img)
            feature.feature("./str/" + file + str(idx), 0)
#seg("fruit")