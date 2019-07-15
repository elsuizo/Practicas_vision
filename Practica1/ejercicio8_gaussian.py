#! /usr/bin/env python

#*************************************************************************
# 8. Hallar un valor de segmentacion optimo (en forma manual o automatica) para
#cada una de las imagenes tomadas en el punto 1 (6 imagenes).
#Mostrar los resultados
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#******************************************************************************

path3 = 'Imagenes/sci-4.bmp'

img3 = cv2.imread(path3, cv2.IMREAD_GRAYSCALE)
img3_bin = np.copy(img3)
img3_bin = cv2.medianBlur(img3_bin, 7)

th3 = cv2.adaptiveThreshold(img3_bin, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
        cv2.THRESH_BINARY, 11, 2)

plt.figure()
plt.imshow(img3, cmap='gray')
plt.figure()
plt.imshow(img3_bin, cmap='gray')
plt.show()
