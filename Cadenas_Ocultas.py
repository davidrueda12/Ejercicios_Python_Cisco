juego = str(input("Digite una palabra: "))
oculto=str(input("Digite la cadena oculta: "))

juego = juego.replace(""," ").split()

y =[]
for i in juego:
    if oculto.find(i) != -1:
        y.append(i)
    else:
        continue

if len(juego) == len(y):
    print("Si")
else:
    print("No")