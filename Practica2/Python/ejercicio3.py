#! /usr/bin/env python


#*************************************************************************
# Mostrar mediante ejemplos los efectos que se producen en el histograma
# de una Imagen al aplicarle una ecualizacion por histograma()
# Implementacion de Opencv
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#*****************************************************************************

path1 = '../Imagenes/sci-2.bmp'
path2 = '../Imagenes/baboon.jpg'

img1 = cv2.imread(path2, 0)

eq = cv2.equalizeHist(img1)

res = np.hstack((img1,eq))

cv2.imwrite('res.png', res)

#-------------------------------------------------------------------------
#                        plots
#-------------------------------------------------------------------------
img_res = cv2.imread('res.png', 0)
plt.figure()
plt.imshow(img_res, cmap='gray')
plt.title('Ecualizacion de histograma(Opencv function)')
plt.figure()
plt.hist(img1.flatten(), 256, [0,256], color='r')
plt.title('Histograma de Imagen')
plt.figure()
plt.hist(eq.flatten(), 256, [0,256], color='r')
plt.title('Histograma ecualizado')
plt.show()

