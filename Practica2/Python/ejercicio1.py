#! /usr/bin/env python

#*************************************************************************
# Mostrar mediante ejempos los efectos que se producen en el histograma de
# imagen al modificarle su brillo y su contraste
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#*****************************************************************************


def imadjust(imagen, low_in, hig_in, low_out, hig_out, gamma):
    """docstring for imadjust
    Implementacion de la funcion de Matlab imadjust, ver Gonzalez-Goods
    """
    imagen_mod = np.zeros(imagen.shape, dtype=np.uint8)

    imagen_mod = low_out + (hig_out - low_out) * ((imagen - low_in) / (hig_in - low_in)) ** gamma


    return imagen_mod

def histograma(imagen):
    """Funcion para calcular el histograma de una imagen"""
    h = np.zeros(256, dtype=float)
    imagen = imagen.astype(np.uint8)
    for i in range(256):
        x = np.array([])
        x = np.argwhere(imagen== i)
        if (len(x) == 0):
            continue
        h[i] = len(x)/float(imagen.size)  # Normalizamos
    return h

path1 = '../Imagenes/galaxy2_gray.jpg'
path2 = '../Imagenes/baboon.jpg'

img1 = cv2.imread(path1, 0)
J = imadjust(img1, .5, .75, .3, 1, .3)
print(J)
hist1 = histograma(img1)
hist2 = histograma(J)

#-------------------------------------------------------------------------
#                        plots
#-------------------------------------------------------------------------
plt.figure()
plt.imshow(J, cmap='gray')
plt.figure()
plt.imshow(img1, cmap='gray')
plt.figure()
plt.stem(np.arange(256), hist1, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.figure()
plt.stem(np.arange(256), hist2, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.show()
