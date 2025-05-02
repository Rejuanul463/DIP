import random
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

imgfive = img.copy()
imgThree = img.copy()
imgSeven = img.copy()

def avarage(image , x , y, t):
    it = [[-1,0,-1], [-2, -1, 0, 1, 2], [-3, -2, -1, 0, 1, 2, 3]]
    sz = 0
    if(t == 0):
        sz = 9
    if(t == 1):
        sz = 25
    if(t == 2):
        sz = 49
    out = 0
    for i in(it[t]):
        for j in(it[t]):
            ix = x + i
            iy = y + j
            if((ix > 0 and ix < size) and (iy > 0 and iy < size)):
                out += image[ix][iy]/sz
            else:
                out += image[x][y]/sz
    return out

def avgFilter():
    for i in range(size):
        for j in range(size):
            imgfive[i][j] = avarage(img, i, j, 1)
            imgThree[i][j] = avarage(img, i, j, 0)
            imgSeven[i][j] = avarage(img, i, j, 2)


avgFilter()

plt.figure(figsize=(16,16))
plt.subplot(2,2,1)
plt.imshow(img, cmap='grey')
plt.title('Original Image')

plt.subplot(2,2,2)
plt.imshow(imgThree, cmap='grey')
plt.title('Image After 3*3 avarage filter')

plt.subplot(2,2,3)
plt.imshow(imgfive, cmap='grey')
plt.title('Image After 5*5 avarage filter')

plt.subplot(2,2,4)
plt.imshow(imgSeven, cmap='grey')
plt.title('Image After 7*7 avarage filter')

plt.show()