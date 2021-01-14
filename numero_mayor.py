#Presentaremos varias formas de encontrar el numero mayor:
# 1. Condicionales if:
# lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))
numero4 = int (input("Ingresa el cuarto número:"))
numero5 = int (input("Ingresa el quinto número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario y asi en todos los casos
if numero2 > nmasGrande:
    nmasGrande = numero2

if numero3 > nmasGrande:
    nmasGrande = numero3

if numero4 > nmasGrande:
    nmasGrande = numero4

if numero5 > nmasGrande:
    nmasGrande = numero5

#imprimir el resultado
print("El número más grande es:",nmasGrande)

# 2. Funcion Max():
# lee tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))
numero4 = int (input("Ingresa el cuarto número:"))
numero5 = int (input("Ingresa el quinto número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3,numero4,numero5)

# imprimir el resultado
print("El número más grande es:", numeroMayor)

# 3. Ciclo while:
# Almacenaremos el número más grande actual aquí

numero = int(input ("Introduzca un número positivo o escriba 0 para detener:"))
numeroMayor = 0

# Si el número no es igual a -1, continuaremos
while numero != 0:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
        numero = int (input("Introduce un número o escribe 0 para detener:"))

    if numero < 0:
        print("Debe ingresar numeros positivos")
        # Ingresa el siguiente número
        numero = int (input("Introduce un número o escribe 0 para detener:"))

# Imprimir el número más grande
print("El numero más grande es:", numeroMayor)