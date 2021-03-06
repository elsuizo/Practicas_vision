#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:38:05 2013

@author: elsuizo
"""
#Ejercicio 2
#Mostrar el efecto del ruido producido por en una imagen que se toma con bajas
#condiciones de luminosidad

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#******************************************************************************

#imagen sacada con bajo nivel de iluminacion
path3 = '../Imagenes/sci-4.bmp'

#vamos a demostrar como se amplifica el ruido en el sensor ccd

img3_opencv = cv2.imread(path3, 0)
img3_matplot = mpimg.imread(path3)  # leemos con matplotlib(python puro)

#extraigo toda la fila 37
row_37 = img3_opencv[37, :]  # Slicing

#plots
#******************************************************************************
fig, array_ax = plt.subplots(1, 3)
array_ax[0].plot(row_37)
array_ax[1].imshow(img3_opencv)
array_ax[2].imshow(img3_matplot)
plt.show()
