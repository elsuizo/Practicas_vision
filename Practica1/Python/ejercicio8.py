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


def segmentacion_auto_Gonz(image):
    """
    Funcion para obtener el valor de segmentacion automaticamente
    Entrada: imagen (escala de grises)
    Salida: T (valor de segmentacion)
    """

    T = 0.5*(np.min(image)+np.max(image))
    flag = False
    while not flag:
        g = image >= T
        T_next = 0.5*(np.mean(image[g])+np.mean(image[np.invert(g)]))
        flag = np.abs(T-T_next) < 0.5
        T = T_next
    return T


path1 = 'Imagenes/sci-2.bmp'
path2 = 'Imagenes/sci-3.bmp'
path3 = 'Imagenes/sci-4.bmp'
path4 = 'Imagenes/tar-5.bmp'
path5 = 'Imagenes/tar-6.bmp'
path6 = 'Imagenes/tar-7.bmp'

img1 = cv2.imread(path1, cv2.CV_LOAD_IMAGE_GRAYSCALE)
img2 = cv2.imread(path2, cv2.CV_LOAD_IMAGE_GRAYSCALE)
img3 = cv2.imread(path3, cv2.CV_LOAD_IMAGE_GRAYSCALE)
img4 = cv2.imread(path4, cv2.CV_LOAD_IMAGE_GRAYSCALE)
img5 = cv2.imread(path5, cv2.CV_LOAD_IMAGE_GRAYSCALE)
img6 = cv2.imread(path6, cv2.CV_LOAD_IMAGE_GRAYSCALE)

T1 = segmentacion_auto_Gonz(img1)
T2 = segmentacion_auto_Gonz(img2)
T3 = segmentacion_auto_Gonz(img3)
T4 = segmentacion_auto_Gonz(img4)
T5 = segmentacion_auto_Gonz(img5)
T6 = segmentacion_auto_Gonz(img6)


print T1
print T2
print T3
print T4
print T5
print T6
img1_bin = img1 < T1
img2_bin = img2 < T2
img3_bin = img3 < T3
img4_bin = img4 < T4
img5_bin = img5 < T5
img6_bin = img6 < T6
#plots

plt.figure()
plt.imshow(img1_bin, cmap='gray')
plt.figure()
plt.imshow(img2_bin, cmap='gray')
plt.figure()
plt.imshow(img3_bin, cmap='gray')
plt.figure()
plt.imshow(img4_bin, cmap='gray')
plt.figure()
plt.imshow(img5_bin, cmap='gray')
plt.figure()
plt.imshow(img6_bin, cmap='gray')

plt.show()
