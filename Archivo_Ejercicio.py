from os import read, strerror
# Ejecicio de archivos: 
#Pida al usuario el nombre del archivo de entrada, lea el archivo (si es posible) y cuente todas las 
# letras latinas (las letras mayúsculas y minúsculas se tratan como iguales). Imprima un histograma 
# simple en orden alfabético (solo se deben presentar recuentos distintos de cero). El histograma de 
# salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero). 
# El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión 
# '.hist' (debe concatenarse con el nombre original).
try:
    dic = {}
    contador = 0
    stream = open("ejemplo_write.txt", "rt")
    y = stream.read(1)
    
    while y != '':
        contador += 1
        y = stream.read(1)

    stream.close()

    stream = open("ejemplo_write.txt", "rt")
    x = stream.read(0)

    for x in stream.read(10000).lower():

        if x in dic.keys():
            dic[x] += 1
        else:
            dic[x] = 1
    stream.close()

    dic_ordenado=sorted(dic)
    print("Caracteres en el archivo: ", contador)

    dic1 = sorted(dic.items(),key=lambda x:x[1], reverse=True)

    #Imprimir los elementos en diccionario
    '''for i in dic_ordenado:
        print(i,"->",dic[i])'''
    #Imprime los elementos del resultado de una lista con tuplas por el resultado del sorted
    #el cual ordena los valores de mayor a menor
    for i in dic1:
        print(i[0],"->",i[1])

    new = open("ejemplo_write.hist", 'wt')
    for i in dic1:
        new.write(str(i[0])+"->"+str(i[1])+"\n")
    new.close()

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))