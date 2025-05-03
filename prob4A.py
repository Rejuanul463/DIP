import imageio
import matplotlib.pyplot as plt
import numpy as np


image = imageio.imread('character.tif')
h,w = image.shape

def applyIdealHighPassFilter(fftImage, radius):
    high = np.zeros((h, w))

    for u in range(h):
        for v in range(w):
            D = np.sqrt((u-h/2)**2 + (v-w/2)**2)
            if(D > radius):
                high[u][v] = 1

    highpass = np.fft.ifft2(np.fft.ifftshift(fftImage * high))

    return np.abs(highpass)

def applyGausianFilter(fftImage, radius):
    gausianFilter = np.zeros((h,w), dtype= np.float32)

    for u in range(h):
        for v in range(w):
            D = np.sqrt((u - h/2) ** 2 + (v - w/2) ** 2)
            gausianFilter[u][v] = 1 - np.exp(-(D**2) / (2 * (radius**2)))

    filteredImage = np.fft.ifft2(np.fft.ifftshift(fftImage * gausianFilter))

    return np.abs(filteredImage)


gausianNoise = np.random.normal(7, 13, image.shape).astype(np.uint8)
noisyImage = image + gausianNoise

noisyImageFFT = np.fft.fftshift(np.fft.fft2(noisyImage))
imagefft = np.fft.fftshift(np.fft.fft2(image.copy()))

idealHighPassFilteredImage = applyIdealHighPassFilter(noisyImageFFT.copy(), 30)
gausianHighPassFilteredImage = applyGausianFilter(noisyImageFFT.copy(), 30)

plt.figure(figsize=(16,16))
plt.subplot(2,4,1)
plt.imshow(image,cmap='grey')

plt.subplot(2,4,2)
plt.imshow(noisyImage, cmap='grey')

plt.subplot(2,4,3)
plt.imshow(np.log(abs(noisyImageFFT)), cmap='grey')

plt.subplot(2,4,4)
plt.imshow(idealHighPassFilteredImage, cmap='grey')

plt.subplot(2,4,5)
plt.imshow(gausianHighPassFilteredImage, cmap='grey')

idealHighPassFilteredImage = applyIdealHighPassFilter(imagefft.copy(), 30)
gausianHighPassFilteredImage = applyGausianFilter(imagefft.copy(), 30)

plt.subplot(2,4,6)
plt.imshow(idealHighPassFilteredImage, cmap='grey')

plt.subplot(2,4,7)
plt.imshow(gausianHighPassFilteredImage, cmap='grey')

plt.show()