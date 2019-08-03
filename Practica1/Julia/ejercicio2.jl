#= -------------------------------------------------------------------------
# @file ejercicio2.jl
#
# @date 08/03/19 14:50:45
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
using Images, PyPlot
# Ejercicio 2
# Mostrar el efecto del ruido producido por en una imagen que se toma con bajas
# condiciones de luminosidad

# imagen obtenida con bajo nivel de iluminacion
path3 = "../Imagenes/sci-3.bmp"
img = load(path3)
row_37 = channelview(img[37, :])
row_37_red = row_37[1, :]

# ya que la iluminacion es deficiente vamos a demostrar que el ruido afecta a la medicion del ccd
plot(row_37_red)
