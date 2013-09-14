/*Ejercicio1 :
Ejercicio 1 Practica 1
Adquirir tres imagenes en tonalidad de grises de dos objetos distintos con
ilumninacion de intensidad baja, media y alta.
*/
#include <opencv2/opencv.hpp>
#include<stdio.h>


using namespace std;
using namespace cv;

int main()

{
    //Mat es la clase madre de Opencv2
    Mat imagen1, imagen2, imagen3, imagen4,imagen5, imagen6;
    string path1, path2, path3, path4, path5, path6;

    path1 = "Imagenes/sci-2.bmp";
    path2 = "Imagenes/sci-3.bmp";
    path3 = "Imagenes/sci-4.bmp";
    path4 = "Imagenes/tar-5.bmp";
    path5 = "Imagenes/tar-6.bmp";
    path6 = "Imagenes/tar-7.bmp";


    imagen1 = imread(path1,0) ;// 0=grayscale, >0 Color image, <0 con alpha chanel
    imagen2 = imread(path2,0) ;
    imagen3 = imread(path3,0) ;
    imagen4 = imread(path4,0) ;
    imagen5 = imread(path5,0) ;
    imagen6 = imread(path6,0) ;

    // Es necesario crear las ventanas donde vamos a alojar las imagenes
    namedWindow("Imagen1");
    namedWindow("Imagen2");
    namedWindow("Imagen3");
    namedWindow("Imagen4");
    namedWindow("Imagen5");
    namedWindow("Imagen6");

    imshow("Imagen1",imagen1);
    imshow("Imagen2",imagen2);
    imshow("Imagen3",imagen3);
    imshow("Imagen4",imagen4);
    imshow("Imagen5",imagen5);
    imshow("Imagen6",imagen6);

    //Hay que poner un waitkey para que no desaparezcan las ventanas
    waitKey(0);
    destroyAllWindows();

    return (0);
}
