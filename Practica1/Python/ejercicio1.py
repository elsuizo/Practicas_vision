#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:49:11 2013

@author: elsuizo

"""
#Ejercicio 1 Practica 1
#Adquirir tres imagenes en tonalidad de grises de dos objetos distintos con
#ilumninacion de intensidad baja, media y alta.

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
#******************************************************************************

path1 = 'Imagenes/sci-2.bmp'
path2 = 'Imagenes/sci-3.bmp'
path3 = 'Imagenes/sci-4.bmp'
path4 = 'Imagenes/tar-5.bmp'
path5 = 'Imagenes/tar-6.bmp'
path6 = 'Imagenes/tar-7.bmp'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
img3 = cv2.imread(path3)
img4 = cv2.imread(path4)
img5 = cv2.imread(path5)
img6 = cv2.imread(path6)

#Mostramos las imagenes

fig, axarr = plt.subplots(2, 3)
axarr[0, 0].imshow(img1)
axarr[0, 0].set_title('Figura 1')
axarr[0, 1].imshow(img2)
axarr[0, 1].set_title('Figura 2')
axarr[0, 2].imshow(img3)
axarr[0, 2].set_title('Figura 3')
axarr[1, 0].imshow(img4)
axarr[1, 0].set_title('Figura 4')
axarr[1, 1].imshow(img5)
axarr[1, 1].set_title('Figura 5')
axarr[1, 2].imshow(img6)
axarr[1, 2].set_title('Figura 6')
plt.show()
