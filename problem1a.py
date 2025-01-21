import imageio as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("D:\RizwanDIP\grayImg.bmp")

size = 256
im = [[0] * size for _ in range(size)]
size = int(size/2)
im1 = [[0] * size for _ in range(size)]
size = int(size/2)
im2 = [[0] * size for _ in range(size)]

for i in range(512-1):
    for j in range(512-1):
        if i % 2 == 0 and j % 2 == 0 :
            val = (img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])
            im[int(i/2)][int(j/2)] = img[i][j]

for i in range(256-1):
    for j in range(256-1):
        if i % 2 == 0 and j % 2 == 0 :
            val = (img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])
            im1[int(i/2)][int(j/2)] = im[i][j]

for i in range(128-1):
    for j in range(128-1):
        if i % 2 == 0 and j % 2 == 0 :
            val = (img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])
            im2[int(i/2)][int(j/2)] = im1[i][j]



plt.figure(figsize=(20,20))
plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.imshow(im)
plt.subplot(2,2,3)
plt.imshow(im1)
plt.subplot(2,2,4)
plt.imshow(im2)
# print(im)

plt.show()

