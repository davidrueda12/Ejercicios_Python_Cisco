#from modulo import suml, prodl
from sys import path

path.append('C:\\Users\\Usuario\\Desktop\\Ejercicios MinTIC2022\\python\\Cisco\\Ejercicios_Python_Cisco')

import modulo

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo.suml(zeroes))
print(modulo.prodl(ones))