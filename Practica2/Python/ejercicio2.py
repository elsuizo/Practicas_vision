#! /usr/bin/env python


#*************************************************************************
# Modificar el brillo y el contraste a las Imagenes tomadas en TP1 de manera
# que se puedan apreciar la mayor cantidad de detalles(tener en cuenta el
# histograma)
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#*****************************************************************************

# FIXME(elsuizo:2019-07-16): me tira un warning de que para algunos valores divide por cero!!!
def contrast_stretch(imagen, m, E):
    """docstring for contrast_stretch"""
    epsilon = np.finfo(np.float).eps
    g = 1 / (1 + (m / imagen + epsilon) ** E)
    return g.astype(np.uint8)

path1 = '../Imagenes/sci-2.bmp'

path2 = '../Imagenes/baboon.jpg'
img1 = cv2.imread(path1, 1)

g1 = contrast_stretch(img1, .1, 9)

#-------------------------------------------------------------------------
#                        plots
#-------------------------------------------------------------------------
plt.figure()
plt.imshow(img1, cmap='gray')
plt.figure()
plt.imshow(g1, cmap='gray')
plt.show()
