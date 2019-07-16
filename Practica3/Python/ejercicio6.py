#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# 6. Implementar un algoritmo que permita realizar una búsqueda de
# patrones utilizando tratamiento de imágenes en el dominio de la frecuencia.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
#*****************************************************************************

# TODO(elsuizo:2019-07-16): a esto habia que hacerlo con la fft y un patron

path1 = '../Imagenes/baboon.jpg'
path2 = '../Imagenes/ojo_baboon.png'
img1 = cv2.imread(path2, 0)
mask = cv2.imread(path2, 0)





