# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.

userWord = str(input("Ingrese una palabra: "))

userWord = userWord.upper()

for i in userWord:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    else:
        print(i,"",end="")


    