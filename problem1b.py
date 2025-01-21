import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("D:/RizwanDIP/cat.bmp")

size = 512
im = [[0] * size for _ in range(size)]
im1 = [[0] * size for _ in range(size)]
im2 = [[0] * size for _ in range(size)]
im3 = [[0] * size for _ in range(size)]
im4 = [[0] * size for _ in range(size)]
im5 = [[0] * size for _ in range(size)]
im6 = [[0] * size for _ in range(size)]
im7 = [[0] * size for _ in range(size)]
imOriginal = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(img.shape[1]):
        im[i][j] = img[i][j] & 128
        im1[i][j] = img[i][j] & 64
        im2[i][j] = img[i][j] & 32
        im3[i][j] = img[i][j] & 16
        im4[i][j] = img[i][j] & 8
        im5[i][j] = img[i][j] & 4
        im6[i][j] = img[i][j] & 2
        im7[i][j] = img[i][j] & 1
        imOriginal[i][j] = im[i][j] + im1[i][j] + im2[i][j] + im3[i][j] + im4[i][j] + im5[i][j] + im6[i][j]


plt.figure(figsize=(15,15))
plt.subplot(3,4,1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.subplot(3,4,2)
plt.title('For MSB 7th bit')
plt.imshow(im, cmap='gray')
plt.subplot(3,4,3)
plt.title('For 6th bit')
plt.imshow(im1, cmap='gray')
plt.subplot(3,4,4)
plt.title('For 5th bit')
plt.imshow(im2, cmap='gray')
plt.subplot(3,4,5)
plt.title('For 4th bit')
plt.imshow(im3, cmap='gray')
plt.subplot(3,4,6)
plt.title('For 3th bit')
plt.imshow(im4, cmap='gray')
plt.subplot(3,4,7)
plt.title('For 2th bit')
plt.imshow(im5, cmap='gray')
plt.subplot(3,4,8)
plt.title('For 1th bit')
plt.imshow(im6, cmap='gray')
plt.subplot(3,4,9)
plt.title('For LSB 0th bit')
plt.imshow(im7, cmap='gray')
plt.subplot(3,4,10)
plt.title('After Summing MSB to LSB')
plt.imshow(imOriginal, cmap='gray')


plt.show()
