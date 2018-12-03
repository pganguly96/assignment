import cv2
import numpy as np
from matplotlib import pyplot as plt

def inverse(file):
    img = cv2.imread(file + ".jpg",0)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    if (file[:2] == "./"):
        file = file[5:]
    np.savetxt("./textureAndShape/inverse/" + file + "Inverse.csv", img)
    rows, cols = img.shape
    crow, ccol = rows / 2, cols / 2
    fshift[int(crow - 30):int(crow + 30), int(ccol - 30):int(ccol + 30)] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    np.savetxt("./textureAndShape/reverse/" + file + "Reverse.csv", img)
#inverse("fruit")