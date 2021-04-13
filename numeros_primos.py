#Imprime una lista de los numeros primos que existen hasta el numero digitado.
n = int(input("Digite un numero: "))

var= 0
for i in range(2, n + 1):
    primos = True
    for x in range(2,11):
        if i == x:
            continue
        elif i % x == 0:
            primos = False
        else:
            continue
    if primos == True:
        print(i," ", end='')
        var += 1
print("\nHay",var, "numeros primos")

