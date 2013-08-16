#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
#Mostrar un ejemplo de la aplicación de la “magnitud del gradiente” 
#para resaltar bordes.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#*****************************************************************************


path1 = 'Imagenes/opensource-softwares2.jpg'
path2 = 'Imagenes/Rana2.bmp'

img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

kernel_grad = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
img2_grad = cv2.filter2D(img1, -1, kernel_grad)

plt.figure()
plt.imshow(img1, cmap='gray')
plt.title('Imagen original')
plt.figure()
plt.imshow(img2_grad, cmap='gray')
plt.title('Magnitud del gradiente')
plt.show()

