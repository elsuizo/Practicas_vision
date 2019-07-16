# Ejercicio 1

#  Adquirir 3 imagenes en tonalidades de gris de 2 objetos distintos con
#  iluminación de intensidad baja, media y alta (total: 6 imagenes).

using Images
using ImageView

# load paths
path1 = "../Imagenes/sci-2.bmp";
path2 = "../Imagenes/sci-3.bmp";
path3 = "../Imagenes/sci-4.bmp";
path4 = "../Imagenes/tar-5.bmp";
path5 = "../Imagenes/tar-6.bmp";
path6 = "../Imagenes/tar-7.bmp";

# read the Images
img1 = load(path1);
img2 = load(path2);
img3 = load(path3);
img4 = load(path4);
img5 = load(path5);
img6 = load(path6);

