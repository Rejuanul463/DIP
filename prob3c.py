import random
import cv2
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import statistics

img = iio.imread("grayImg.bmp")
size = 512

def addNoise(imag):
    for i in range(10000):
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        imag[x][y] = 255
    for i in range(10000):
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        imag[x][y] = 0
    return imag


img = addNoise(img)
imgHarAvgFilter = img.copy()
imgGeoAvgFilter = img.copy()

def geoAvarage(image , x , y):
    mul = 1/25
    it = {-2, -1, 0, 1, 2}
    out = 1.0
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < size) and (iy > 0 and iy < size)):
                out *= image[ix][iy] ** mul
            else:
                out *= image[x][y] ** mul
    return out

def harAvarage(image , x , y):
    mul = 25
    it = {-2, -1, 0, 1, 2}
    out = 0
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < size) and (iy > 0 and iy < size)):
                if(image[ix][iy].any() > 0):
                    out += 1 / image[ix][iy]
            else:
                if (image[x][y].any() > 0):
                    out += 1 / image[x][y]

    out = mul / out
    return out

def AvgFilter(imag, geo):
    for i in range(size):
        for j in range(size):
            if(geo):
                imag[i][j] = geoAvarage(img, i, j)
            else:
                imag[i][j] = harAvarage(img, i, j)
    return imag

imgGeoAvgFilter = AvgFilter(imgGeoAvgFilter , True)
imgHarAvgFilterFilter = AvgFilter(imgHarAvgFilter, False)


plt.figure(figsize=(16,16))
plt.subplot(1,3,1)
plt.imshow(img, cmap='grey')
plt.title('Original Image')

plt.subplot(1,3,2)
plt.imshow(imgGeoAvgFilter, cmap='grey')
plt.title('Image After Geometric Mean filter')

plt.subplot(1,3,3)
plt.imshow(imgHarAvgFilterFilter, cmap='grey')
plt.title('Image After Harmonic Mean filter')

plt.show()