import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("cat.bmp")
size = 512

imMSB3 = [[0] * size for _ in range(size)]
imDif = [[0] * size for _ in range(size)]

shift = 8-3

for i in range(size):
    for j in range(img.shape[1]):
        imMSB3[i][j] = (img[i][j] >> shift) << shift
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


