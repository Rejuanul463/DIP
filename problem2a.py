import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("cat.bmp")
size = 512

rangeMin = 50
rangeMax = 150

plt.subplot(2,1,1)
plt.imshow(img, cmap='grey')

for i in range(size):
    for j in range(size):
        if(img[i][j] <= rangeMax and img[i][j] >= rangeMin):
            img[i][j] = img[i][j] + 50

plt.subplot(2,1,2)
plt.imshow(img, cmap='grey')
plt.show()