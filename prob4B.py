import random
import cv2
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import statistics

img = iio.imread("grayImg.bmp", pilmode='L')
size = 512

def add_gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape).astype(np.float32)
    noisy = image.astype(np.float32) + noise
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return noisy

noisyImage = add_gaussian_noise(img.copy())

dft = np.fft.fft2(noisyImage.copy())
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)



plt.figure(figsize=(16,16))
plt.subplot(2,2,1)
plt.imshow(img, cmap='grey')
plt.title('Original Image')

plt.subplot(2,2,2)
plt.imshow(noisyImage, cmap='grey')
plt.title('Noisy Image')

plt.show()