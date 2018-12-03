import cv2
import numpy as np
def rgb(file):
    img = cv2.imread(file + ".jpg")
    if (file[:2] == "./"):
        file = file[5:]
    np.savetxt("./color/fruit/blue/" + file + "RGB.csv", img[:, :, 0], delimiter=",")
    np.savetxt("./color/fruit/green/" + file + "RGB.csv", img[:, :, 1], delimiter=",")
    np.savetxt("./color/fruit/red/" + file + "RGB.csv", img[:, :, 2], delimiter=",")
#rgb("red")
