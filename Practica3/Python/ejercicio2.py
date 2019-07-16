#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# 2. Crear en el dominio de la frecuencia un filtro pasabajos ideal,
# aplicarlo a una imagen y mostrar el efecto “anillo” que se produce en la
# imagen. Explicar a que se debe.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
#******************************************************************************

path1 = '../Imagenes/baboon.jpg'
path2 = '../Imagenes/Rana2.bmp'
img1 = cv2.imread(path2, 0)
img2 = cv2.imread(path2, 0)

img1_frec = fftpack.fft2(img1)  #fft de la Imagen

#Aplicamos un corrimiento para que solo se visualice un periodo
img1_frec_shift = fftpack.fftshift(img1_frec)

#Aplicamos log para visualizar
img1_log_abs = np.log(1 + np.abs(img1_frec_shift))

img2_frec = fftpack.fft2(img2)
img2_frec_shift = fftpack.fftshift(img2_frec)

rows, cols = img1.shape
crow, ccol = rows/2 , cols/2
# NOTE(elsuizo:2019-07-16):  pasaba que no podiamos indexar con floats, para convertirlo hay que reasignarlo a la variable porque no la modifica!!!
crow = int(crow)
ccol = int(ccol)

# ringing effects, se produce porque estamos convolucionando con una mascara
# cuadrada, que produce una sinc de dos dimensiones
img1_frec_shift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_ishift = np.fft.ifftshift(img1_frec_shift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Imagen despues del filtro pasaalto'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Resultado in JET'), plt.xticks([]), plt.yticks([])

plt.show()
