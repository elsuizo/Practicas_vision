#! /usr/bin/env python
#*************************************************************************
# 4) Desarrollar una funcion que permita realizar el efecto de falso color
# en una imagen dada 
#
#*************************************************************************

#*************************************************************************
# Inports
import numpy as np
import matplotlib.pyplot as plt
import cv2
#*************************************************************************
 
def falso_color(img):
    """docstring for falso_color"""
    
    rows,cols = img.shape
    img_red = np.copy(img)
    img_green = np.copy(img)
    img_blue = np.copy(img)
    img_false = np.zeros((rows, cols, 3), dtype=np.uint8)
    
    for i in xrange(0,rows):
        for j in xrange(0,cols):
        
            if (0<=img[i,j]<=43):
                img_red[i,j] = 255
                img_green[i,j] = img[i,j]*(255/43)
                img_blue[i,j] = 0
            
            elif(43<img[i,j]<=86):
                img_red[i,j] = (255-(img[i,j]-43)*(255/43))
                img_green[i,j]=255
                img_blue[i,j]=0
        
            elif(86<img[i,j]<=128):
                img_red[i,j] = 0
                img_green[i,j] = 255
                img_blue[i,j] = ((img[i,j]-86)*(255/42))
        
            elif(128<img[i,j]<=171):
                img_red[i,j] = 0
                img_green[i,j] = ((171-img[i,j])*(255/43))
                img_blue[i,j] = 255
        
            elif(171<img[i,j]<=214):
                img_red[i,j] = (img[i,j]-171)*(255/43)
                img_green[i,j] = 0
                img_blue[i,j] = 255
        
            elif(214<img[i,j]):
                img_red[i,j] = 255
                img_green[i,j] = 0
                img_blue[i,j] = ((255-img[i,j])*(255/41))
    
    img_false[:,:,0]=img_red
    img_false[:,:,1]=img_green
    img_false[:,:,2]=img_blue

    return img_false

path2 = 'Imagenes/opensource-softwares2.jpg'

image = cv2.imread(path2, 0)

falso = falso_color(image)
cv2.imwrite( 'opensource.png', falso)
#plt.savefig(falso, 'lyapunov_loco.png')
plt.figure()
plt.imshow(image, cmap='gray')
plt.title('Imagen original')
plt.figure()
plt.imshow(falso)
plt.title('Falso color de la imagen')
plt.show()
