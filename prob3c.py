import random
import cv2
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import statistics

img = iio.imread("grayImg.bmp", pilmode='L')
h,w = img.shape

def addNoise(imag):
    for i in range(10000):
        x = random.randint(0,h-1)
        y = random.randint(0,w-1)
        imag[x][y] = 255
    for i in range(10000):
        x = random.randint(0,h-1)
        y = random.randint(0,w-1)
        imag[x][y] = 0
    return imag


img = addNoise(img)
imgHarAvgFilter = img.copy()
imgGeoAvgFilter = img.copy()

def geoAvarage(image , x , y, karnelSize):
    if (karnelSize == 5):
        it = {-2, -1, 0, 1, 2}
    else:
        it = {-1, 0, 1}
    out = 1
    count = 0
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < h) and (iy > 0 and iy < w)):
                if(image[ix][iy]):
                    count += 1
                    out *= int(image[ix][iy])
    out = out ** (1/count)
    return np.uint8(out)

def harAvarage(image , x , y, karnelSize):
    NoofPixels = karnelSize ** 2
    if (karnelSize == 5):
        it = {-2, -1, 0, 1, 2}
    else:
        it = {-1, 0, 1}
    out = 0
    count = 0
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < h) and (iy > 0 and iy < w)):
                if(image[ix][iy] > 0):
                    count += 1
                    out += float(1 / int(image[ix][iy]) + 1e-4)

    out = karnelSize / out
    out = max(0 ,min(255, out))
    return np.uint8(out)

def AvgFilter(imag, geo, karnelSize):
    for i in range(h):
        for j in range(w):
            if(geo):
                imag[i][j] = geoAvarage(img, i, j, karnelSize)
            else:
                imag[i][j] = harAvarage(img, i, j, karnelSize)
    return imag

imgGeoAvgFilter = AvgFilter(imgGeoAvgFilter , True, 3)
imgHarAvgFilterFilter = AvgFilter(imgHarAvgFilter, False, 3)


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
