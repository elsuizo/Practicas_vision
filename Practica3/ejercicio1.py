#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# Escoger una imagen en escala de grises aplicarle la transformada de Fourier 
# y graficar el modulo de dicha transformada.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
# FIXME(elsuizo:2019-07-16): no se porque no anda el error que tira es raro
# cambie de usar la funcion de scipy por la de numpy y tampoco anda
import numpy as np
import matplotlib.pyplot as plt
# from scipy import fftpack
#*****************************************************************************


path1 = '../Imagenes/baboon.jpg'
path2 = '../Imagenes/Rana2.bmp'

img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

# img1_frec = fftpack.fft2(img1)  #fft de la Imagen

img1_f = np.fft.fft2(img1)

#Aplicamos un corrimiento para que solo se visualice un periodo
# img1_frec_shift = fftpack.fftshift(img1_frec)

img1_f_shift = np.fft.fftshift(img1_f)

#Aplicamos log para visualizar
# img1_log_abs = np.log(1 + np.abs(img1_frec_shift))

img1_log_abs = 20 * np.log(np.abs(img1_f_shift))

# img2_frec = fftpack.fft2(img2)
img1_f = np.fft.fft2(img2)
# img2_frec_shift = fftpack.fftshift(img2_frec)
img2_f_shift = np.fft.fftshift(img2_f)
 # Aplicamos log para visualizar
# img2_log_abs = np.log(1 + np.abs(img2_frec_shift))
img2_log_abs = 20 * np.log(np.abs(img2_f_shift))

#-------------------------------------------------------------------------
#                        plots
#-------------------------------------------------------------------------
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
