# Apertura de archivos, stream = open(file, mode = 'r', encoding = None)
# Apertura modo lectura (mode='r'), escritura(mode='w'), adjuntar(mode='a'), 
# leer y actualizar(mode='r+'), escribir y actualizar(mode='w+')
# Si al final de la cadena modo termina en b se abrira de modo binario, si es una t
# se abrira en modo texto

#Esta es una forma simplificada de tratar los errores en archivos, de os importamos el strerror
# el cual nos da el numero del error econtrado y una breve explicacion de este, para esto
# se debe poner como agrumento la excepcion.errno
'''
from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    print("El archivo no se pudo abrir:", strerror(exc.errno))'''

# Ejemplo de lectura de caracteres de una archivo:
from os import read, strerror

try:
    contador = 0
    stream = open("C:\\Users\\Usuario\\Desktop\\Guia de estudio front-end.txt", "rt")
    caracteres = stream.read(1)
    while caracteres != '':
        print(caracteres, end='')
        contador += 1
        caracteres = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo: ", contador)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

# Ejemplo de lectura de lineas de una archivo:

try:
    contador1 = 0
    stream = open("C:\\Users\\Usuario\\Desktop\\Guia de estudio front-end.txt", 'rt')
    lectura = stream.readline()
    while lectura != '':
        contador1 += 1
        lectura = stream.readline()
    stream.close()
    print("Lineas en el archivo:     ", contador1)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

# Ejemplo de uso readlineS:

stream = open("C:\\Users\\Usuario\\Desktop\\Guia de estudio front-end.txt", 'rt')
x = stream.readlines(100)
stream.close()
print(x)
try:
    ccnt = lcnt = 0
    s = open("C:\\Users\\Usuario\\Desktop\\Guia de estudio front-end.txt", 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
        lines = s.readlines(10)
    s.close()
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

# Ejemplo de write():

try:
	fo = open("ejemplo_write.txt", 'wt') # crea un nuevo archivo (ejemplo.txt) 
	fo.write(" Esto es un ejemplo ")
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))

#bytearray: es un arreglo que contiene bytes (amorfos), son mutables, suceptibles a la funcion len()
#y se puede indexar, no se debe establecer ningún elemento del arreglo de bytes con un valor que no sea un entero
#y tampoco está permitido asignar un valor fuera del rango de 0 a 255


data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))

# Con readinto() se leen los archivos binarios:

bf = open('file.bin', 'rb')
bf.readinto(data)
bf.close()

for b in data:
    print(hex(b), end=' ')

# Tambien podemos usar read() que a diferencia de readinto() es inmmutable, si no se le especifica
# la cantidad de bytes a leer tomara todo el archivo, si se le pone, esta sera la cantidad maxima.

bf = open('file.bin', 'rb')
data = bytearray(bf.read())
bf.close()

for b in data:
    print(hex(b), end=' ')