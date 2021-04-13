
def misplit(frase):
    frase= frase.split()
    return frase


while True:
    try:
        frase = str(input("Ingrese una frase: "))
        assert frase.replace(" ","").isalpha() == True
        print(misplit(frase))
        break
    except AssertionError:
        print("Por favor digite solo cadenas,usted digito {}".format(frase))
    except KeyboardInterrupt:
        print("Proceso interrumpido")
        break
    