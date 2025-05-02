import imageio
import matplotlib.pyplot as plt
import numpy as np

def gray_level_segmentation(img):
    result = np.zeros_like(img)
    for i in range(h):
        for j in range(w):
            val = img[i][j]
            if val < 85:
                result[i][j] = 0
            elif val < 170:
                result[i][j] = 150
            else:
                result[i][j] = 255
    return result

img = imageio.imread('image.bmp', pilmode='L')
h,w = img.shape
seg_img = gray_level_segmentation(img)

plt.figure(figsize=(14,7))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(seg_img, cmap='gray')
plt.title('Gray-Level Segmentation')
plt.show()