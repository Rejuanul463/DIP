import imageio
import numpy as np
import matplotlib.pyplot as plt

# Sobel kernels
sobelX = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

sobelY = [[-1, -2, -1],
          [ 0,  0,  0],
          [ 1,  2,  1]]

prewitX = [[-1,0,1],
           [-1,0,1],
           [-1,0,1]]
prewitY = [[-1,-1,-1],
           [0, 0, 0],
           [1, 1, 1]]

laplacian = [[0,-1,0],
             [-1,4,-1],
             [0,-1,0]]

def applyLaplacian(imag, x, y, karnel):
    ar = [-1,0,1]
    out = 0
    for i in(ar):
        for j in(ar):
            ix = x + i
            iy = y + j
            if(0<=ix<h and 0<=iy<w):
                out += int(imag[ix][iy]) * karnel[i+1][j+1]
            else:
                out += int(imag[x][y]) * karnel[i+1][j+1]
    return max(0,min(155,out))

def laplacianFilter(imag):
    result = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            result[i][j] = np.uint8(applyLaplacian(imag, i, j, laplacian))
    return result
def applyPrewit(imag, x, y, filter):
    ar = [-1,0,1]
    out = 0
    for i in(ar):
        for j in(ar):
            ix = x + i
            iy = y + i
            if(0 <= ix < h and 0 <= iy < w):
                out += int(imag[ix][iy]) * filter[i+1][j+1]
            else:
                out += int(imag[x][y]) * filter[i+1][j+1]
    out = max(0 , min(255,out))
    return out

def prewitFilter(imag):
    result = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            ix = applyPrewit(imag, i, j, sobelX)
            iy = applyPrewit(imag, i, j, sobelY)
            mag = (ix**2 + iy**2)** (0.5)
            result[i][j] = np.uint8(mag)

    return result

def applySobel(imag, x, y, kernel):
    ar = [-1, 0, 1]
    out = 0
    for i in ar:
        for j in ar:
            ix = x + i
            iy = y + j
            if (0 <= ix < h) and (0 <= iy < w):
                out += int(imag[ix][iy]) * kernel[i+1][j+1]
            else:
                out += int(imag[x][y]) * kernel[i+1][j+1]
    out = max(0, min(255, out))
    return out

def sobelFilter(imag):
    result = np.zeros_like(imag)
    for i in range(h):
        for j in range(w):
            gx = applySobel(imag, i, j, sobelX)
            gy = applySobel(imag, i, j, sobelY)
            mag = (gx**2 + gy**2)**0.5
            result[i][j] = np.uint8(min(255, mag))
    return result

# Load grayscale image using imageio
img = imageio.imread('grayImg.bmp', pilmode='L')
h, w = img.shape

# Apply Sobel filter
sobel_result = sobelFilter(img)
prewitResult = prewitFilter(img)
laplacianResult = laplacianFilter(img)

# Show result using matplotlib
plt.figure(figsize=(16,16))
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('original image')

plt.subplot(2,2,2)
plt.imshow(sobel_result, cmap='gray')
plt.title('Sobel Edge Detection')

plt.subplot(2,2,3)
plt.imshow(prewitResult, cmap='gray')
plt.title('prewit Edge Detection')

plt.subplot(2,2,4)
plt.imshow(laplacianResult, cmap='gray')
plt.title('Laplacian Edge Detection')

plt.show()
