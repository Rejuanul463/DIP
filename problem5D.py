import imageio
import matplotlib.pyplot as plt
import numpy as np

def addShade(img):
    for i in range(h):
        for j in range(w):
            if (j >= w / 2):
                img[i][j] += 20
    return img

def adaptive_threshold(img, t1, t2):
    result = np.zeros_like(img)
    for i in range(h):
        for j in range(w):
            if(j < w/2):
                result[i][j] = 255 if(img[i][j] > t1) else  0
            else:
                result[i][j] = 255 if (img[i][j] > t2) else 0
    return result

def global_threshold(img, T=127):
    result = np.zeros_like(img)
    for i in range(h):
        for j in range(w):
            result[i][j] = 255 if img[i][j] >= T else 0
    return result

img = imageio.imread('threshold.tif')

h,w = img.shape
img = addShade(img)
binary_img = adaptive_threshold(img, 40, 80)
gBinary_img = global_threshold(img , 60)
plt.figure(figsize=(14,7))
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1,3,2)
plt.imshow(binary_img, cmap='gray')
plt.title('adaptive Thresholding')

plt.subplot(1,3,3)
plt.imshow(gBinary_img, cmap='gray')
plt.title('Global Thresholding')

plt.show()