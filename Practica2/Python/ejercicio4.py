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


# NOTE(elsuizo:2019-07-16): notar que esta es una malisima implementacion!!!
def falso_color(img):
    """Dada una imagen, se la transforma a falso color"""
    rows,cols = img.shape
    img_red = np.copy(img)
    img_green = np.copy(img)
    img_blue = np.copy(img)
    img_false = np.zeros((rows, cols, 3), dtype=np.uint8)

    for i in range(0,rows):
        for j in range(0,cols):

            if (0 <= img[i, j] <= 43):
                img_red[i, j] = 255
                img_green[i, j] = img[i, j] * (255 / 43)
                img_blue[i, j] = 0

            elif(43 < img[i, j] <= 86):
                img_red[i, j] = (255 - (img[i, j] - 43) * (255 / 43))
                img_green[i, j] = 255
                img_blue[i,j] = 0

            elif(86 < img[i, j] <= 128):
                img_red[i, j] = 0
                img_green[i, j] = 255
                img_blue[i, j] = ((img[i, j] - 86) * (255 / 42))

            elif(128<img[i, j]<=171):
                img_red[i, j] = 0
                img_green[i, j] = ((171 - img[i, j]) * (255 / 43))
                img_blue[i, j] = 255

            elif(171 < img[i, j] <= 214):
                img_red[i, j] = (img[i, j] - 171) * (255 / 43)
                img_green[i, j] = 0
                img_blue[i, j] = 255

            elif(214 < img[i, j]):
                img_red[i, j] = 255
                img_green[i, j] = 0
                img_blue[i, j] = ((255 - img[i, j]) * (255 / 41))

    img_false[:, :, 0] = img_red
    img_false[:, :, 1] = img_green
    img_false[:, :, 2] = img_blue

    return img_false

# NOTE(elsuizo:2019-07-16): esta es la manera que se debe calcular el falso color mediante una lookup-table
def false_color_fast(img):
    """
    Function for calculate a false color of a image

    Input:
    -----
    img: grayscale image

    output:
    ------
    img_fc: 3-channel false color image

    """
    # red LUT
    red = np.zeros(256, dtype="uint8")
    red[0:43] =  255
    red[43:86] = np.arange(43, 0, -1) * (255.0 / 43.0)
    red[172:215] = np.arange(0, 43) * (255.0 / 43.0)
    red[214:] = 255
    # green LUT
    green = np.zeros(256, dtype="uint8")
    green[0:43] = np.arange(43) * (255.0 / 43.0)
    green[43:129] = 255
    green[129:172] = np.arange(43, 0, -1) * (255.0 / 43.0)
    # blue LUT
    blue = np.zeros(256, dtype="uint8")
    blue[86:129] = np.arange(43) * (255.0 / 43.0)
    blue[129:213] = 255
    blue[213:] = np.arange(43, 0, -1) * (255 / 43.0)

    m,n = img.shape
    img_fc = np.zeros((m, n, 3))

    img_fc_r = cv2.LUT(img, red)
    img_fc_g = cv2.LUT(img, green)
    img_fc_b = cv2.LUT(img, blue)
    img_fc = cv2.merge((img_fc_r, img_fc_g, img_fc_b))

    return img_fc


path2 = '../Imagenes/opensource-softwares2.jpg'

image = cv2.imread(path2, 0)

#-------------------------------------------------------------------------
#                        plots
#-------------------------------------------------------------------------
falso = falso_color(image)
cv2.imwrite( 'opensource.png', falso)
#plt.savefig(falso, 'lyapunov_loco.png')
plt.figure()
plt.imshow(image, cmap='gray')
plt.title('Imagen original')
plt.figure()
plt.imshow(falso)
plt.title('Falso color de la imagen')

false = false_color_fast(image)
cv2.imwrite( 'opensource_fast.png', false)
#plt.savefig(falso, 'lyapunov_loco.png')
plt.figure()
plt.imshow(image, cmap='gray')
plt.title('Imagen original')
plt.figure()
plt.imshow(false)
plt.title('Falso color de la imagen con la funcion false_color_fast')
plt.show()
