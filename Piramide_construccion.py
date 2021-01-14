bloques = int(input("Introduzca el número de bloques disponibles: "))
 
altura = 0
# Bloques usados por fila
utilizados = 0
# Cantidad de bloques que se requieren cara cada fila
por_fila = 1
construccion = True 

while construccion == True:
    utilizados += por_fila
    if utilizados > bloques:
        construccion = False
 
    altura += 1
    por_fila += 1
 
print("La altura de la pirámide es de:", altura)