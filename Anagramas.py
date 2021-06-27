import unicodedata

while True:
    try:
        palabra = str(input("Escriba dos palabras: "))

        assert palabra.replace(" ","").isalpha() == True 

        #Metodo para eliminar los acentos y caracteres con acento de las frases segun Unicode.
        palabra = ''.join((c for c in unicodedata.normalize('NFD',palabra) if unicodedata.category(c) != 'Mn'))
        palabra = palabra.lower().replace(".","").split()
        
        assert (len(palabra) > 2) != True
        
        x=0
        y=0

        for i in palabra[0]:
            x += ord(i)

        for i in palabra[1]:
            y += ord(i)

        if x == y:
            print("Anagramas")
        else:
            print("No Anagramas")
        break

    except AssertionError:
        print("Por favor solo digite textos y solo 2 palabras")
    except KeyboardInterrupt:
        print("Proceso interrumpido")
        break
