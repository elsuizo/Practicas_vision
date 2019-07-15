# /usr/bin/env python

#*************************************************************************
# 6. Desarrollar una funcion que permita calcular el histograma de una imagen
# en tonos de gris y lo muestre en pantalla.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#******************************************************************************


def histograma(img):
    """Docstring de la funcion"""
    h = np.zeros(256, dtype=float)
    for i in range(256):
        x = np.array([])
        x = np.argwhere(img == i)
        if (len(x) == 0):
            continue
        h[i] = len(x) / float(img.size)  # Normalizamos
    return h

path1 = 'Imagenes/sci-2.bmp'
path2 = 'Imagenes/sci-3.bmp'
path3 = 'Imagenes/sci-4.bmp'
path4 = 'Imagenes/tar-5.bmp'
path5 = 'Imagenes/tar-6.bmp'
path6 = 'Imagenes/tar-7.bmp'

img1 = cv2.imread(path1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(path3, cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread(path4, cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread(path5, cv2.IMREAD_GRAYSCALE)
img6 = cv2.imread(path6, cv2.IMREAD_GRAYSCALE)


hist1 = histograma(img1)
hist2 = histograma(img2)
hist3 = histograma(img3)
hist4 = histograma(img4)
hist5 = histograma(img5)
hist6 = histograma(img6)


#plots
plt.figure()
plt.stem(np.arange(256), hist1, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Histograma de imagen1')
plt.figure()
plt.stem(np.arange(256), hist2, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Histograma de imagen2')
plt.figure()
plt.stem(np.arange(256), hist3, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Histograma de imagen3')
plt.figure()
plt.stem(np.arange(256), hist4, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Histograma de imagen4')
plt.figure()
plt.stem(np.arange(256), hist5, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Histograma de imagen5')
plt.figure()
plt.stem(np.arange(256), hist6, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Histograma de imagen6')
plt.show()
