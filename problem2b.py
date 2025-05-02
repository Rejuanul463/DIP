#brightenning dark sides of the image
import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("cat.bmp")

img_normilized = img / 255.0
gamma = 0.5
gamma1 = 2
c = 1
size = 512
imgPowerLawWithNegGamma = [[0] * size for _ in range(size)]
imgInverseLog = [[0] * size for _ in range(size)]
imgPowerLawWithPosGamma = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        imgPowerLawWithNegGamma[i][j] = c * pow(img_normilized[i][j], gamma)
        imgPowerLawWithPosGamma[i][j] = c * pow(img_normilized[i][j], gamma1)
        imgInverseLog[i][j] = np.exp(img_normilized[i][j] / c)

plt.subplot(2,2,1)
plt.title("Original Image")
plt.imshow(img_normilized, cmap='grey')
plt.subplot(2,2,2)
plt.title("Using Power Law (Gamma < 1)")
plt.imshow(imgPowerLawWithNegGamma, cmap='grey')
plt.subplot(2,2,3)
plt.title("Using Power Law (Gamma > 1)")
plt.imshow(imgPowerLawWithPosGamma, cmap='grey')
plt.subplot(2,2,4)
plt.title("using Inverse logarithm")
plt.imshow(imgInverseLog, cmap='grey')
plt.show()