import imageio as iio
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = iio.imread("grayImg.bmp")
#array
histogram = np.zeros(256)
size = 512 - 1

# compute histogram
for i in range(size):
    for j in range(size):
        intensity = img[i][j]
        histogram[intensity] += 1

threshold = 128

binaryImage = (img > threshold) * 255

# Plot histogram manually
plt.figure(figsize=(10, 5))
plt.subplot(2,2,3)
plt.bar(range(256), histogram, width=1, color='gray')
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.subplot(2,2,1)
plt.title("Image")
plt.imshow(img, cmap='grey')
plt.subplot(2,2,2)
plt.title("Threshold Image")
plt.imshow(binaryImage, cmap='grey')
plt.show()