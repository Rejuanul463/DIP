import imageio
import matplotlib.pyplot as plt
import numpy as np


image = imageio.imread('gray.png', pilmode='L')
h,w = image.shape

def applyButterWorthFilter(fftImage, order, redius):
    butterWorthFilter = np.zeros((h, w), dtype=float)

    for i in range(h):
        for j in range(w):
            D = ((i-h/2) ** 2 + (j-w/2) ** 2) ** 0.5
            butterWorthFilter[i][j] = 1 / (1 + (D/redius) ** (2 * order))

    filteredImage = np.fft.ifft2(np.fft.ifftshift(fftImage * butterWorthFilter))

    return np.abs(filteredImage)

def applyGausianFilter(fftImage, radius):
    gausianFilter = np.zeros((h,w), dtype= np.float32)

    for u in range(h):
        for v in range(w):
            D = np.sqrt((u - h/2) ** 2 + (v - w/2) ** 2)
            gausianFilter[u][v] = np.exp(-(D**2) / (2 * (radius**2)))

    filteredImage = np.fft.ifft2(np.fft.ifftshift(fftImage * gausianFilter))

    return np.abs(filteredImage)

def apply_gaussian_filter(image, cutoff_freq):
    height, width = image.shape
    gaussian_filter = np.zeros((height, width), dtype = np.float32)

    for u in range(height):
        for v in range(width):
            D = np.sqrt((u - height / 2)**2 + (v - width / 2)**2)
            gaussian_filter[u, v] = np.exp(-(D**2) / (2 * (cutoff_freq**2)))

    filtered_image = image * gaussian_filter
    filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_image))
    return np.abs(filtered_image)


gausianNoise = np.random.normal(7, 13, image.shape).astype(np.uint8)
noisyImage = image + gausianNoise

noisyImageFFT = np.fft.fftshift(np.fft.fft2(noisyImage))

butterWorthImage = applyButterWorthFilter(noisyImageFFT.copy(), 4, 30)
gausianImage = applyGausianFilter(noisyImageFFT.copy(), 30)

plt.figure(figsize=(16,16))
plt.subplot(2,3,1)
plt.imshow(image,cmap='grey')

plt.subplot(2,3,2)
plt.imshow(noisyImage, cmap='grey')

plt.subplot(2,3,3)
plt.imshow(np.log(abs(noisyImageFFT)), cmap='grey')

plt.subplot(2,3,4)
plt.imshow(butterWorthImage, cmap='grey')

plt.subplot(2,3,5)
plt.imshow(gausianImage, cmap='grey')

plt.show()