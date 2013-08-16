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
from scipy import fftpack
#*****************************************************************************

path1 = 'Imagenes/baboon.jpg'
path2 = 'Imagenes/Rana2.bmp'
img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

img1_frec=fftpack.fft2(img1)
img1_frec_shift = fftpack.fftshift(img1_frec)
 # Aplicamos log para visualizar
img1_log_abs = np.log(1+np.abs(img1_frec_shift)) 

img2_frec=fftpack.fft2(img2)
img2_frec_shift = fftpack.fftshift(img2_frec)
 # Aplicamos log para visualizar
img2_log_abs = np.log(1+np.abs(img2_frec_shift)) 

plt.figure()
plt.imshow(img1, cmap='gray')
plt.title('Imagen 1')
plt.figure()
plt.imshow(img1_log_abs, cmap='gray')
plt.title('Imagen 1 dominio frecuencia')

plt.figure()
plt.imshow(img2, cmap='gray')
plt.title('Imagen 2')
plt.figure()
plt.imshow(img2_log_abs, cmap='gray')
plt.title('Imagen 2 dominio frecuencia')

plt.show()


