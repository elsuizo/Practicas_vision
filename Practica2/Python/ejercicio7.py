#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
#Aplicar el filtro promediador a 2 imágenes (en escalas de grises) distintas.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#*****************************************************************************

def ker_prom(n):
    ker = np.ones((n,n))
    ker_promedio = ker/np.size(ker)
    return ker_promedio

path1 = 'Imagenes/baboon.jpg'
path2 = 'Imagenes/Rana2.bmp'

img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

prom1= cv2.filter2D(img1, -1, ker_prom(4))

prom2= cv2.filter2D(img2, -1, ker_prom(4))

plt.figure()
plt.imshow(img1, cmap='gray')
plt.title('Imagen1 original')
plt.figure()
plt.imshow(prom1, cmap='gray')
plt.title('Imagen1 filto promediador')
plt.figure()
plt.imshow(img2, cmap='gray')
plt.title('Imagen2 original')
plt.figure()
plt.imshow(prom2, cmap='gray')
plt.title('Imagen2 filto promediador')
plt.show()



