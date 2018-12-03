import cv2
import numpy as np
def var(file):
    img = cv2.imread(file + ".jpg")
    [B, G, R] = list(np.array(img).mean(axis = (0, 1)))
    #print(B)
    #print(G)
    #print(R)
    r = (B/(B + G + R))
    g = (G/(B + G + R))
    b = (B/(B + G + R))
    gradRed = 0
    gradBlue = 0
    gradGreen = 0
    n = img[:, :, 0].size
    for a in img[:, :, 0]:
        for i in a:
            #print(i)
            gradBlue = gradBlue + (((i - B)*(i - B))/n)
    for a in img[:, :, 1]:
        for i in a:
            gradGreen = gradGreen + (((i - G)*(i - G))/n)
    for a in img[:, :, 2]:
        for i in a:
            gradRed = gradRed + (((i - R)*(i - R))/n)
    #print(gradRed)
    arr = np.array([R, G, B, r, g, b, gradRed, gradGreen, gradBlue])
    #print(arr)
    if (file[:2] == "./"):
        file = file[5:]
    np.savetxt("./color/gradient/" + file + "gradient.csv", arr)
#var("fruit")