#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# Para dos Imágenes distintintas (en escala de grises) acentuar los bordes
# utilizando los filtros “Laplacian Sharpening” y “Hight Boost Filter”
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#*****************************************************************************

path1 = 'Imagenes/baboon.jpg'
path2 = 'Imagenes/Rana2.bmp'

img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

#Utilizamos las herramientas de Opencv
laplaciano = cv2.Laplacian(img2, -1)
#Una alternativa es usar filter2d ingresando el kernel correspondiente
ker_laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplaciano2 = cv2.filter2D(img2, -1, ker_laplacian)

ker_hb = lambda A: np.array([[0,-1,0],[-1,A+4,-1],[0,-1,0]])
img2_hb = cv2.filter2D(img2, -1, ker_hb(1))

plt.figure()
plt.imshow(laplaciano, cmap='gray')
plt.title('Laplaciano')
plt.figure()
plt.imshow(laplaciano2, cmap='gray')
plt.title('Laplaciano mediante kernel')
plt.figure()
plt.imshow(img2_hb, cmap='gray')
plt.title('Hight Boost Filter(A=1)')
plt.show()

