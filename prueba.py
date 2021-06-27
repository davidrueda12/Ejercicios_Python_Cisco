S=input("Ingrese nemonicos de soporte:")
I=input("Ingrese nemonicos de infraestructura:")
D=input("Ingrese las letras de los sevicios:")
S=S.replace(" ","") #quita espacios entre elementos de la variable
I=I.replace(" ","")
D=D.replace(" ","")

soporte=S.upper() #Convierte a mayusculas los string
infra=I.upper()
servicios=D.upper()
contar_s=0
contador_i=0
lista=[]

for i in servicios:
    if i in soporte and i in infra:
        contador_i +=1
        contar_s+=1
    elif i in soporte:
        contar_s += 1
    elif i in infra:
        contador_i+=1

    if contar_s==contador_i:
        lista.append("E") #Agrega elementos a la lista
        #print("E",end="")
    elif contar_s>contador_i:
        lista.append("S")
        #print("S",end="")
    elif contador_i>contar_s:
        lista.append("I")
        #print("I",end="")

resultado="".join(lista) #Agrupa los elementos de una lista en un string
print(resultado)