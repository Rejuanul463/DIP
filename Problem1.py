import imageio as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("D:\RizwanDIP\img.bmp")
img2 = img
for i in range(10):
    for j in range(10):
        img2[i][j] = img[9 - i][j]

img2[9][9] = img[0][9]

plt.imshow(img2)
print(img)

plt.show()

