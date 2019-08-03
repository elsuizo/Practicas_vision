#= -------------------------------------------------------------------------
# @file ejercicio3.jl
#
# @date 08/03/19 18:20:17
# @author Martin Noblia
# @email mnoblia@disroot.org
#
# @brief
#
# @detail
#
#  Licence:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License

---------------------------------------------------------------------------=#
# 4. Mostrar el efecto de descomponer una imagen color con el formato bmp en sus
# tres canales (R,G,B)  y compararla con la original (Se entregaran imagenes de
# prueba para realizar este punto).

#=------------------------------------------------------------------------------
                        imports
------------------------------------------------------------------------------=#
using Images, ImageView
#=------------------------------------------------------------------------------
                        code
------------------------------------------------------------------------------=#
#Imagen de prueba
path1 = "../Imagenes/Lapices.bmp"

img = load(path1)
# utilizamos la notacion de element-wise aplicado sobre cada elemento del array
img_red = red.(img) # extraemos el canal rojo
img_green = green.(img) # extraemos el canal verde
img_blue = blue.(img) # extraemos el canal azul
#=------------------------------------------------------------------------------
                        show results
------------------------------------------------------------------------------=#
imshow(img)
imshow(img_red)
imshow(img_green)
imshow(img_blue)

