#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# 5-Aplicar el operador Laplaciano en el dominio de la frecuencia para 
# destacar detalles en una imagen.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack


#cargamos las Imagenes
path1 = 'Imagenes/baboon.jpg'
path2 = 'Imagenes/Rana2.bmp'
img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)



F1 = fftpack.fft2(img1)
F2 = fftpack.fft2(img2)

F1_shift = np.fft.fftshift(F1)
F2_shift = np.fft.fftshift(F2)

#Utilizamos las herramientas de Opencv
laplaciano1 = cv2.Laplacian(np.abs(F1_shift), -1)
laplaciano2 = cv2.Laplacian(np.abs(F2_shift), -1)

#Una alternativa es usar filter2d ingresando el kernel correspondiente
#ker_laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])
#laplaciano1 = cv2.filter2D(np.abs(F1_shift), -1, ker_laplacian)
#laplaciano2 = cv2.filter2D(np.abs(F2_shift), -1, ker_laplacian)

img1_back = np.fft.ifft2(laplaciano1)
img1_back = np.abs(img1_back)
img2_back = np.fft.ifft2(laplaciano2)
img2_back = np.abs(img2_back)

# Plots
plt.figure()
plt.subplot(221),plt.imshow(img1, cmap = 'gray')
plt.title('Imagen Original 1'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img1_back, cmap = 'gray')
plt.title('Laplaciano 1 en frecuencia'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img2,cmap='gray')
plt.title('Imagen Original 2'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img2_back,cmap='gray')
plt.title('Laplaciano 2 en frecuencia'), plt.xticks([]), plt.yticks([])

plt.figure()
plt.imshow(img1_back,cmap='gray')


plt.show()



