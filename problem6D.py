import imageio
import matplotlib.pyplot as plt
import numpy as np

def isHit(imag, x, y, karnel):
    ar = [-1,0,1]
    for i in(ar):
        for j in(ar):
            ix = x + i;
            iy = y + j;
            if(0<= ix < h and 0 <= iy < w):
                if((karnel[i+1][j+1] == 1 and imag[ix][iy] == 0)):
                    return True
    return False

def dialition(imag, karnel):
    result = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            if(isHit(imag, i, j, karnel) == False):
                result[i][j] = 255
    return result

def regionFilling(imag):
    # step1
    inv = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            if(imag[i][j] == 0):
                inv[i][j] = 255

    #step 2
    result = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            if(i != 2 and j != 2):
                result[i][j] = 255
    # step 2
    karnel = [[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]]
    for k in range(20):
        prev = result
        dil = dialition(result, karnel)
        for i in range(h):
            for j in range(w):
                if(dil[i][j] == 0 and inv[i][j] == 0):
                    result[i][j] = 0

    return result

img = imageio.imread("region.png", pilmode="L")
h,w = img.shape
filledImage = regionFilling(img)


plt.figure(figsize=(14,7))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(filledImage, cmap='gray')
plt.title('Filled Image')
plt.show()