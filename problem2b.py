#brightenning dark sides of the image
import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("D:/RizwanDIP/cat.bmp")

img_normilized = img / 255.0
gamma = 0.5
gamma1 = 1.5
c = 1
size = 512
im = [[0] * size for _ in range(size)]
im1 = [[0] * size for _ in range(size)]
im2 = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        im[i][j] = c * pow(img_normilized[i][j], gamma)
        im2[i][j] = c * pow(img_normilized[i][j], gamma1)
        im1[i][j] = np.exp(img_normilized[i][j] / c)


plt.subplot(2,2,1)
plt.title("Original Image")
plt.imshow(img_normilized, cmap='grey')
plt.subplot(2,2,2)
plt.title("Using Power Law (Gamma < 1)")
plt.imshow(im, cmap='grey')
plt.subplot(2,2,3)
plt.title("Using Power Law (Gamma > 1)")
plt.imshow(im2, cmap='grey')
plt.subplot(2,2,4)
plt.title("using Inverse logarithm")
plt.imshow(im1, cmap='grey')
plt.show()