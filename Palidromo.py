#Ejecicio de verificacion si una palabra o frase es palíndromo o no.

import unicodedata

palabra = str(input("Escriba una palabra o frase: "))
cadena = str(palabra)
#Metodo para eliminar los acentos y caracteres con acento de las frases segun Unicode.
palabra = ''.join((c for c in unicodedata.normalize('NFD',palabra) if unicodedata.category(c) != 'Mn'))

palabra = palabra.lower().replace(""," ").replace(".","").split()

if palabra == palabra[::-1]:
    print("La cadena \"{}\" es un palíndromo".format(cadena))
else:
    print("La cadena \"{}\" no es un palíndromo".format(cadena))




