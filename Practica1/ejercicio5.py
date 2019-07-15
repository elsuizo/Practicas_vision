#! /usr/bin/env python

#*************************************************************************
#Muestreo y Cuantizacion
#5. Mostrar los efectos del muestreo y la cuantizacion en una imagen dada.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#******************************************************************************

# imagen sacada con bajo nivel de iluminacion
path1 = 'Imagenes/Globos.bmp'
img1 = cv2.imread(path1, cv2.IMREAD_GRAYSCALE)
img1_muestreada = np.zeros_like(img1)
#Slicing
img1_muestreada[0:-1:4, 0:-1:4] = img1[0:-1:4, 0:-1:4]

# cuantizacion
niveles = 2
I_cuant = np.floor(img1 * ((256 / niveles) - 1))

# plotting
plt.figure()
plt.imshow(img1_muestreada, cmap='gray')
plt.title('Imagen submuestreada')
plt.figure()
plt.imshow(I_cuant, cmap='gray')
plt.title('Imagen cuantizada')
plt.figure()
plt.imshow(img1, cmap='gray')
plt.title('Imagen original')
plt.show()
