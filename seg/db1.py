import numpy as np
import pywt
import cv2

def w2d(file, mode='db1', level=10):
    print(file)
    imArray = cv2.imread(file + ".jpg")
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_BGR2GRAY )
    #convert to float
    imArray =  np.float32(imArray)
    imArray /= 255
    # compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)
    #Process Coefficients
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0
    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H =  np.uint8(imArray_H)
    #Display result
    if (file[:2] == "./"):
        file = file[5:]
    np.savetxt("./textureAndShape/db1/" + file + "Db1.csv", imArray_H)

#w2d("fruit",'db1',10)