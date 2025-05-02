import imageio.v2 as iio
import numpy as np
import matplotlib.pyplot as plt

img = iio.imread("cat.bmp")

bit_levels = 8

plt.figure(figsize=(15, 15))

for b in range(bit_levels, 0, -1):
    bitsToRemove = 8 - b
    # Right and Left shift to remove lowerbits
    reducedImage = (img >> bitsToRemove) << bitsToRemove

    plt.subplot(3, 3, 9 - b)
    plt.title(f'{b}-bit Resolution')
    plt.imshow(reducedImage, cmap='gray')
    plt.axis('off')

binary_img = (img > 128) * 255
plt.subplot(3, 3, 9)
plt.title('1-bit (Binary)')
plt.imshow(binary_img, cmap='gray')
plt.axis('off')

plt.show()
