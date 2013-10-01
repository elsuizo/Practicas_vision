#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# 1. A partir de una imagen en escala de grises generar 10 imágenes con 
# ruido gaussiano. 
#*************************************************************************


#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Funciones
#******************************************************************************

def imnoise(im, sigma, mu):
    
    M, N = im.shape
    R = (sigma * np.random.rand(M,N) + mu) + im
    
    return R

#******************************************************************************
   
path1 = 'Imagenes/baboon.jpg'
path2 = 'Imagenes/Rana2.bmp'
img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

for x in range(0,9):
    globals()['R' + str(x)] = imnoise(img1,100*x,10+x)


for i in range(0,9):
    ax = plt.subplot(3,3,i)
    ax.imshow(globals()['R' + str(i)],cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
