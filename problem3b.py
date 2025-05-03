import random
import imageio
import numpy as np
import matplotlib.pyplot as plt
import statistics

image = imageio.imread("grayImg.bmp", pilmode='L')
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

def computePsnr(original, filtered):
    original, filtered = np.float64(original), np.float64(filtered)
    mse = np.mean((original - filtered) ** 2)

    if(mse == 0):
        return inf
    else:
        psnr = 20 * np.log10(255.0) - 10 * np.log10(mse)

    return round(psnr, 2)


avgFilter()

psnr3 = computePsnr(image, imgThree)
psnr5 = computePsnr(image, imgfive)
psnr7 = computePsnr(image, imgSeven)

print(psnr3)
print(psnr5)
print(psnr7)

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
