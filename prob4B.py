import imageio
import matplotlib.pyplot as plt
import numpy as np


image = imageio.imread('character.tif')
h,w = image.shape

def applyIdealFilter(fftImage, radius):
    low = np.zeros((h, w))

    for u in range(h):
        for v in range(w):
            D = np.sqrt((u-h/2)**2 + (v-w/2)**2)
            if(D <= radius):
                low[u][v] = 1

    lowPass = np.fft.ifft2(np.fft.ifftshift(fftImage * low))

    return np.abs(lowPass)


gausianNoise = np.random.normal(7, 13, image.shape).astype(np.uint8)
noisyImage = image + gausianNoise

noisyImageFFT = np.fft.fftshift(np.fft.fft2(noisyImage))

idealLowPass10 = applyIdealFilter(noisyImageFFT.copy(), 10)
idealLowPass20 = applyIdealFilter(noisyImageFFT.copy(), 20)
idealLowPass30 = applyIdealFilter(noisyImageFFT.copy(), 30)

plt.figure(figsize=(16,16))
plt.subplot(2,3,1)
plt.imshow(image,cmap='grey')

plt.subplot(2,3,2)
plt.imshow(noisyImage, cmap='grey')

plt.subplot(2,3,3)
plt.imshow(np.log(abs(noisyImageFFT)), cmap='grey')

plt.subplot(2,3,4)
plt.imshow(idealLowPass20, cmap='grey')

plt.subplot(2,3,5)
plt.imshow(idealLowPass30, cmap='grey')

plt.subplot(2,3,6)
plt.imshow(idealLowPass10, cmap='grey')

plt.show()