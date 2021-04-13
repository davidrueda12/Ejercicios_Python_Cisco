#Ejemplo manejo del try-except, ejercicio de raiz cuadrada de un numero decimal.
import math
y = True
while y == True:
    try:
        x = float(input("Ingresa un numero: "))
        assert x >= 0.0 and x < 100000
        x = math.sqrt(x)
        print(x)
        y = False

    except ValueError:
        print("Por favor digite solo numeros")
    except AssertionError:
        print("Por favor digite un numero mayor a 0 y menor a 100000, el numero que usted digito es {}".format(x))
    except KeyboardInterrupt: #imprime el mensaje si se sale del proceso con ctrl+c
        print("Proceso interrumpido")
        y = False







