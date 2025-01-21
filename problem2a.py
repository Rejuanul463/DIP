#brightenning dark sides of the image
import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("D:/RizwanDIP/cat.bmp")

size = 512
im = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if(img[i][j] <= 150 and img[i][j] >= 50):
            im[i][j] = img[i][j] + 50
        else:
            im[i][j] = img[i][j]

plt.subplot(2,1,1)
plt.imshow(img, cmap='grey')
plt.subplot(2,1,2)
plt.imshow(im, cmap='grey')
plt.show()