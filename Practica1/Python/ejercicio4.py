#! /usr/bin/env python

#*************************************************************************
#
#4. Mostrar el efecto de descomponer una imagen color con el formato bmp en sus
#tres canales (R,G,B)  y compararla con la original (Se entregaran imagenes de
#prueba para realizar este punto).
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#******************************************************************************
#Imagen de prueba
path1 = 'Imagenes/Lapices.bmp'
#leemos la imagen
img1 = cv2.imread(path1)
#prealocamos las imagenes que vamos a usar
img1_red = np.zeros_like(img1)
img1_blue = np.zeros_like(img1)
img1_green = np.zeros_like(img1)
#Copiamos los canales en las imagenes respectivas
img1_red[:, :, 0] = img1[:, :, 0]
img1_green[:, :, 1] = img1[:, :, 1]
img1_blue[:, :, 2] = img1[:, :, 2]

#Mostramos las imagenes
plt.figure()
plt.imshow(img1)
plt.title('Imagen Original')
plt.figure()
plt.imshow(img1_blue)
plt.title('Canal Azul')
plt.figure()
plt.imshow(img1_green)
plt.title('Canal Verde')
plt.figure()
plt.imshow(img1_red)
plt.title('Canal Rojo')
plt.show()
