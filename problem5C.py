import imageio
import matplotlib.pyplot as plt
import numpy as np

def global_threshold(img, T=127):
    result = np.zeros_like(img)
    for i in range(h):
        for j in range(w):
            result[i][j] = 255 if img[i][j] >= T else 0
    return result

img = imageio.imread('image.bmp', pilmode='L')
h,w = img.shape
binary_img = global_threshold(img, T=127)

plt.figure(figsize=(14,7))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(binary_img, cmap='gray')
plt.title('Global Thresholding')
plt.axis('off')
plt.show()