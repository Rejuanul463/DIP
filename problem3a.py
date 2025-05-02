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

imgAvgFilter = img
imgMedFilter = img

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
    it = {-2, -1, 0, 1, 2}
    values = []
    for i in(it):
        for j in(it):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < size) and (iy > 0 and iy < size)):
                values.append(image[ix][iy])
            else:
                values.append(image[x][y])
    # print(values)
    return  values[int(len(values)/2)]

def medianFilter(imag):
    for i in range(size):
        for j in range(size):
            imag[i][j] = findMediun(img, i, j)
    return imag

imgAvgFilter = avgFilter(imgAvgFilter)
imgMedFilter = medianFilter(imgMedFilter)

def calculate_psnr(original, filtered):
    mse = np.mean((original - filtered) ** 2)
    if mse == 0:
        return float('inf')  # No noise
    psnr = 10 * np.log10((255 ** 2) / mse)
    return psnr

psnr_avg = calculate_psnr(img, imgAvgFilter)
psnr_median = calculate_psnr(img, imgMedFilter)

print(f"PSNR (Average Filter): {psnr_avg:.2f} dB")
print(f"PSNR (Median Filter): {psnr_median:.2f} dB")

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