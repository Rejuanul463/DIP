import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("D:/RizwanDIP/cat.bmp")

size = 512
im1 = [[0] * size for _ in range(size)]
im2 = [[0] * size for _ in range(size)]
im3 = [[0] * size for _ in range(size)]

imMSB3 = [[0] * size for _ in range(size)]
imDif = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(img.shape[1]):
        im3[i][j] = img[i][j] & 32
        im2[i][j] = img[i][j] & 64
        im1[i][j] = img[i][j] & 128
        imMSB3[i][j] = im1[i][j] + im2[i][j] + im3[i][j]
        imDif[i][j] = img[i][j] - imMSB3[i][j]


plt.subplot(2,2,1)
plt.imshow(img, cmap='grey')
plt.title("original Image")
plt.subplot(2,2,2)
plt.imshow(imMSB3, cmap='grey')
plt.title("Image Obtained by 3 MSB")
plt.subplot(2,2,3)
plt.imshow(imDif, cmap='grey')
plt.title("difference image")

plt.show()


