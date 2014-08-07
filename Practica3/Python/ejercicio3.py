#! /usr/bin/env python
# -*- coding: utf-8 -*-

#*************************************************************************
# 3- Comparar los efectos de aplicar filtros “pasabajos ideal“,
# “pasabajos Butterworth” y “pasabajos Gausseano”.
#*************************************************************************

#Imports
#******************************************************************************
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

#******************************************************************************
# Funciones
#******************************************************************************

def dftuv(M,N):
    """
    Funcion para realizar meshgrids de frecuencias(Gonzalez, Goods, pag:128)
    Parametros:
    ------------------------------------------------------------------------
    M : entero
    Dimension en U
    N : entero
    Dimension en V
    Salida
    ------------------------------------------------------------------------
    meshgrid ---> U, V

    """
    u = np.arange(0,M)
    v = np.arange(0,N)
    
    idx = np.where(u >= M/2)
    u[idx] = u[idx] - M
    idy = np.where(v >= N/2)
    v[idy] = v[idy] - N
    
    V, U = np.meshgrid(v,u)
    
    return V,U

def lpfilter_ideal(im,D_0):
    """ """
    M,N = im.shape
    U,V = dftuv(M,N)
    
    D = np.sqrt(U**2 + V**2)
    
    H = (D <= D_0)
    H_shift = np.fft.fftshift(H)
    
    F = fftpack.fft2(im)
    F_shift = np.fft.fftshift(F)

    im_fil = H_shift * F_shift

    im_back = np.fft.ifft2(im_fil)

    im_back = np.abs(im_back)
    
    return im_back

def lpfilter_butterworth(im,D_0,n):
    """ """
    M,N = im.shape
    U,V = dftuv(M,N)
    
    D = np.sqrt(U**2 + V**2)
    
    H = 1/(1 + (D/D_0)**(2*n))
    H_shift = np.fft.fftshift(H)
    
    F = fftpack.fft2(im)
    F_shift = np.fft.fftshift(F)

    im_fil = H_shift * F_shift

    im_back = np.fft.ifft2(im_fil)

    im_back = np.abs(im_back)
    
    return im_back

def lpfilter_gaussian(im,D_0):
    """ """
    M,N = im.shape
    U,V = dftuv(M,N)
    
    D = np.sqrt(U**2 + V**2)
    #mascara gaussiana
    H = np.exp((-D**2 )/ (2 * D_0**2))
    H_shift = np.fft.fftshift(H)
    
    F = fftpack.fft2(im)
    F_shift = np.fft.fftshift(F)

    im_fil = H_shift * F_shift

    im_back = np.fft.ifft2(im_fil)

    im_back = np.abs(im_back)
    
    return im_back
#******************************************************************************

#cargamos las Imagenes
path1 = 'Imagenes/baboon.jpg'
path2 = 'Imagenes/Rana2.bmp'
img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

D_0 = 20 #cut-off frecuency
# filtramos en frecuencia con cada filtro a las Imagenes
#imagen 1
img1_lp_ideal = lpfilter_ideal(img1, D_0)
img1_lp_butt = lpfilter_butterworth(img1,D_0,5)
img1_lp_gauss = lpfilter_gaussian(img1,D_0)
#Imagen 2
img2_lp_ideal = lpfilter_ideal(img2, D_0)
img2_lp_butt = lpfilter_butterworth(img2,D_0,5)
img2_lp_gauss = lpfilter_gaussian(img2,D_0)


#******************************************************************************
# Plots
plt.figure()
plt.subplot(221),plt.imshow(img1, cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img1_lp_ideal, cmap = 'gray')
plt.title('Filtro pasabajos ideal'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img1_lp_butt,cmap='gray')
plt.title('Filtro pasabajos Butterworth'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img1_lp_gauss,cmap='gray')
plt.title('Filtro pasabajos Gausseano'), plt.xticks([]), plt.yticks([])

plt.figure()
plt.subplot(221),plt.imshow(img2, cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img2_lp_ideal, cmap = 'gray')
plt.title('Filtro pasabajos ideal'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img2_lp_butt,cmap='gray')
plt.title('Filtro pasabajos Butterworth'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img2_lp_gauss,cmap='gray')
plt.title('Filtro pasabajos Gausseano'), plt.xticks([]), plt.yticks([])

plt.show()
