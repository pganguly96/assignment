import cv2
import numpy as np
def map(file):
    img = cv2.imread(file + ".jpg")
    [B, G, R] = list(np.array(img).mean(axis=(0, 1)))
    arr = np.genfromtxt("configure.csv", delimiter=",", dtype="int32")
    str = []
    #print(arr)
    if len(arr.shape)>1:
        sum = [[0]*11]*arr.shape[0]
        for i in range(0, arr.shape[0]):
            str = arr[i, :]
            sum[i][0] = R*G*B*str[0]
            sum[i][1] = R*R*str[1]
            sum[i][2] = G*G*str[2]
            sum[i][3] = B*B*str[3]
            sum[i][4] = R*G*str[4]
            sum[i][5] = R*B*str[5]
            sum[i][6] = G*B*str[6]
            sum[i][7] = R*str[7]
            sum[i][8] = G*str[8]
            sum[i][9] = B*str[9]
            sum[i][10] = str[10]
    if len(arr.shape) == 1:
        sum = [0]*11
        sum[0] = R*G*B*arr[0]
        sum[1] = R*R*arr[1]
        sum[2] = G*G*arr[2]
        sum[3] = B*B*arr[3]
        sum[4] = R*G*arr[4]
        sum[5] = R*B*arr[5]
        sum[6] = G*B*arr[6]
        sum[7] = R*arr[7]
        sum[8] = G*arr[8]
        sum[9] = B*arr[9]
        sum[10] = arr[10]
    if (file[:2] == "./"):
        file = file[5:]
    np.savetxt("./color/mapping/" + file + "Map.csv", sum)
#map("fruit")