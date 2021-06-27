#Digito de vida:
#Este ejercicio consiste en tomas la fecha de nacimiento, sumas todos sus digitos y
#del resultado de este, sumar tambien sus digitos.

fecha = str(input("Digite la fecha de su cumpleaños en formato AAAA/MM/DD: "))
fecha = fecha.replace("/","").replace(""," ").split()
#Forma uno de conseguir la primera suma de fechas
for i in range(len(fecha)):
    fecha[i]= int(fecha[i])
x = 0
y = 0
for i in fecha:
    x += i
    #Forma dos de conseguir la suma de un numero
    y = sum([int(j) for j in str(x)])

print(y)