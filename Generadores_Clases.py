# Un generador es un fragmento de código especializado capaz de producir una serie de valores y 
# controlar el proceso de iteración. El range() es un ejemplo de ello.
# El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las reglas 
# impuestas por el contexto de las sentencias

#En este ejemplo se emplea el modelo de fibonacci y se observa como el objeto iterador se instancia primero,
#luego se invoca el metodo __inter__ para acceder al iterador y luego el metodo next se invoca 9 veces,
#las primeras 8 produce valores y la novena finaliza la iteracion.

class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("Fib iter")
		return self

	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter

object = Class(8)

for i in object:
	print(i)

# Uso de yield: cambiar el return por yield convierte la función en un generador, al hacer
# esto al pasar por yield la funcion no pierde su estado, todos los valores de las variables
# estan congelados y esperan su proxima invocacion

# Ejemplo de creacion de generadores:
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = [x for x in potenciasDe2(5)] #Se pueden usar en listas de comprension 
x = list(potenciasDe2(3))# En listas reales

for i in range(20):
    if i in potenciasDe2(4): #En contextos creados por el operador in
        print(i)

print(t)
print(x)

# Listas de compresion y generadores
lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10)) # al usar () en vez de [] lo convierte en un generador

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()

# La funcion lambda es una funcion anonima(sin nombre),lambda parámetros: expresión,Tal cláusula devuelve 
# el valor de la expresión al tomar en cuenta el valor del argumento lambda actual.

#Ejemplo de como usar lambda: Funcion normal:

def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

def poli(x):
	return 2 * x**2 - 4 * x + 2

imprimirfuncion([x for x in range(-2, 3)], poli)

# Con lambda: Desaparece el poli() ya que solo se usa una vez 
# y es remplazado con lambda para hacer el codigo mas corto y legible

def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

# La funcion map() aplica la función pasada por su primer argumento a todos los elementos de su segundo 
# argumento y devuelve un iterador que entrega todos los resultados de funciones posteriores.

lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()

# La funcion filter() utiliza el mismo esquema que map() pero este filtra su segundo argumento mientras
# es guiado por direcciones que fluyen desde la función especificada en el primer argumento, los elementos
# True de la funcion pasan el filtro, los demas sond escartados.

from random import randint

data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)

