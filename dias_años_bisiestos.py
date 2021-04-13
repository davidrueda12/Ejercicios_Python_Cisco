#Este ejercicio calcula el numero de dias que tiene el mes segun el año digitado,
#puede variar si el año es bisiesto o no, el ejercicio permite digitar 4 años y 4 meses.

f=0
year = []
month =[]
while f<=3:
    anio=int(input("Digite un año: "))
    mes= int(input("Digite el mes: "))
    year.append(anio)
    month.append(mes)
    f +=1


def Year(year):
    resultado=[]
    for i in year:
        if i % 4 == 0 and i % 100 !=0:
            resultado.append(True)
        else:
            resultado.append(False)
    return resultado
    
def Month(month, Year):
    dias = []
    #La funcion zip ayuda a iterar ambas listas para que tome los items en orden
    for i, x in zip(month,Year):
        if x == True:
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                dias.append(31)
            elif i == 4 or i == 6 or i == 9 or i == 11:
                dias.append(30)
            elif (x == True)and (i == 2):
                dias.append(29)
        else:
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                dias.append(31)
            elif i == 4 or i == 6 or i == 9 or i == 11:
                dias.append(30)
            elif i == 2:
                dias.append(29)
    return dias

print("Dias",Month(month,Year(year)))