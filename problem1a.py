import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("grayImg.bmp")

size = 256
imgH = [[0] * size for _ in range(size)]
size = int(size/2)
imQ = [[0] * size for _ in range(size)]
size = int(size/2)
imHQ = [[0] * size for _ in range(size)]

for i in range(512-1):
    for j in range(512-1):
        if i % 2 == 0 and j % 2 == 0 :
            imgH[int(i/2)][int(j/2)] = img[i][j]

for i in range(256-1):
    for j in range(256-1):
        if i % 2 == 0 and j % 2 == 0 :
            imQ[int(i/2)][int(j/2)] = imgH[i][j]

for i in range(128-1):
    for j in range(128-1):
        if i % 2 == 0 and j % 2 == 0 :
            imHQ[int(i/2)][int(j/2)] = imQ[i][j]


plt.figure(figsize=(20,20))
plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.imshow(imgH)
plt.subplot(2,2,3)
plt.imshow(imQ)
plt.subplot(2,2,4)
plt.imshow(imHQ)
# print(im)

plt.show()

