# Cifrado César Mejorado:
# En este ejercicio se mejoro el cifrado dandole un rango que desee escoger la persona
# ademas, diferencia entre mayusculas y minuscilas salta espacios, acepta numeros y 
# caracteres especiales(estos quedan igual) y no repite el proceso cuando se ingresa 
# mal algun dato, dandole la oportunidad de hacerlo de nuevo 

while True:
    try:
        text = input("Ingresa tu mensaje: ")
        number = int(input("Digite el valor a desplazar de 1 a 25: "))
        cifrado = ''
        assert number > 0 and number < 26 != True
        for char in text:
            if not char.isalnum():
                cifrado += char
                continue
            if char.isdigit():
                cifrado += char
                continue
                
            if char.islower():
                code = ord(char) + number
                if code > ord('z'):
                    dif = number-(ord('z')-ord(char))
                    code = ord('a') + dif
                cifrado += chr(code)
            else:
                code = ord(char) + number       
                if code > ord('Z'):
                    dif = number-(ord('Z')-ord(char))
                    code = ord('A') + dif
                cifrado += chr(code)
        print(cifrado)
        break
    except ValueError:
        print("Por favor digite solo numeros enteros en el valor a desplazar")
    except AssertionError:
        print("Por favor digite numeros entre 1 y 25, usted digito es {}".format(number))
    except KeyboardInterrupt: 
        print("Proceso interrumpido")
        break
        