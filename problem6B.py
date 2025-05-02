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

def isFit(imag, x, y, karnel):
    ar = [-1,0,1]
    out = True
    for i in(ar):
        for j in(ar):
            ix = x + i;
            iy = y + j;
            if(0<= ix < h and 0 <= iy < w):
                if((karnel[i+1][j+1] == 1 and imag[ix][iy] > 0)):
                    out = False
                    break

    return out

def erosion(imag, karnel):
    result = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            if(isFit(imag, i, j, karnel) == False):
                result[i][j] = 255
    return result

img = imageio.imread("binary.png", pilmode = "L")
h,w = img.shape

karnel = [[1,1,1],
          [1,1,1],
          [1,1,1]]

ers = erosion(img, karnel)
dial = dialition(img, karnel)

open = dialition(ers, karnel)
close = erosion(dial, karnel)

plt.figure(figsize=(14,7))
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1,3,2)
plt.imshow(open, cmap='gray')
plt.title('Opening')

plt.subplot(1,3,3)
plt.imshow(close, cmap='gray')
plt.title('Closing')

plt.show()