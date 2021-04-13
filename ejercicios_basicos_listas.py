#Ejercicio para ingresar el numero de elementos a una lista y ordenas esos 
# elementos segun su valor en forma de codigo:
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#Forma de ordenas una lista con funciones de python:

miLista = [8, 10, 6, 2, 4]
miLista.sort() #ordena la lista de menor a mayor
print(miLista)
miLista.reverse()#invierte la lista
print(miLista) 

#Encontrar el mayor elemento de una lista:

miLista = [17, 3, 11, 5, 1, 9, 7, 18, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)

#Encontrar elementos de una lista en otra lista:

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)

#Hacer una lista sin elementos repetidos:

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista = []

for i in miLista:
    if i not in lista:
        lista.append(i)

print("La lista solo con elementos únicos:")
print(miLista)
print(lista)