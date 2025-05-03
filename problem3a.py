import random
import cv2
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import statistics

image = iio.imread("grayImg.bmp", pilmode="L")
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


img = addNoise(image.copy())

def avarage(image , x , y):
    it = {-2, -1, 0, 1, 2}
    out = 0
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < size) and (iy > 0 and iy < size)):
                out += image[ix][iy]/25
            else:
                out += image[x][y]/25
    return out

def avgFilter(imag):
    for i in range(size):
        for j in range(size):
            imag[i][j] = avarage(img, i, j)
    return imag

def findMediun(image , x , y):
    it = {-1, 0, 1}
    values = []
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < size) and (iy > 0 and iy < size)):
                values.append(image[ix][iy])
            else:
                values.append(image[x][y])
    return  sorted(values)[int(len(values)/2)]

def medianFilter(imag):
    for i in range(size):
        for j in range(size):
            imag[i][j] = findMediun(img, i, j)
    return imag


imgAvgFilter = avgFilter(img.copy())
imgMedFilter = medianFilter(img.copy())


def compute_psnr(image1, image2):
    image1, image2 = np.float64(image1), np.float64(image2)
    mse = np.mean((image1 - image2) ** 2)
    if mse == 0:
        return float('inf')
    psnr = 20 * np.log10(255.0) - 10 * np.log10(mse)

    return round(psnr, 2)

psnr_avg = compute_psnr(image, imgAvgFilter)
psnr_median = compute_psnr(image, imgMedFilter)

print(psnr_avg)
print(psnr_median)

plt.figure(figsize=(16,16))
plt.subplot(1,3,1)
plt.imshow(img, cmap='grey')
plt.title('Original Image')

plt.subplot(1,3,2)
plt.imshow(imgAvgFilter, cmap='grey')
plt.title('Image After avarage filter')

plt.subplot(1,3,3)
plt.imshow(imgMedFilter, cmap='grey')
plt.title('Image After mediun filter')

plt.show()
