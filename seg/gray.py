import cv2
import numpy as np
def gray(file):
    img = cv2.imread(file + ".jpg")
    img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./color/grayImage/" + file + "Gray.jpg", img)
    if (file[:2] == "./"):
        file = file[5:]
    np.savetxt("./color/grayImage/file/" + file + "Gray.csv", img)
#gray("fruit")