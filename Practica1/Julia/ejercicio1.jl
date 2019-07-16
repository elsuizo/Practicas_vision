# Ejercicio 1

#  Adquirir 3 imagenes en tonalidades de gris de 2 objetos distintos con
#  iluminación de intensidad baja, media y alta (total: 6 imagenes).

import Images
import PyPlot

# Load paths
path1 = "../Imagenes/sci-2.bmp";
path2 = "../Imagenes/sci-3.bmp";
path3 = "../Imagenes/sci-4.bmp";
path4 = "../Imagenes/tar-5.bmp";
path5 = "../Imagenes/tar-6.bmp";
path6 = "../Imagenes/tar-7.bmp";

# Read the Images
img1 = Images.load(path1);
img2 = Images.load(path2);
img3 = Images.load(path3);
img4 = Images.load(path4);
img5 = Images.load(path5);
img6 = Images.load(path6);

# plots with the matplotlib wrapper
# plots con Matplotlib ¡¡¡
fig = PyPlot.figure(figsize=(10,10))
#PyPlot.subplots_adjust(hspace=0.5) # Set the vertical spacing between axes

PyPlot.subplot(231)
PyPlot.title("Figura 1")
PyPlot.imshow(convert(Array,img1))

PyPlot.subplot(232)
PyPlot.title("Figura 2")
PyPlot.imshow(convert(Array,img2))

PyPlot.subplot(233)
PyPlot.title("Figura 3")
PyPlot.imshow(convert(Array,img3))

PyPlot.subplot(234)
PyPlot.title("Figura 4")
PyPlot.imshow(convert(Array,img4))

PyPlot.subplot(235)
PyPlot.title("Figura 5")
PyPlot.imshow(convert(Array,img5))

PyPlot.subplot(236)
PyPlot.title("Figura 6")
PyPlot.imshow(convert(Array,img6))

PyPlot.show()
