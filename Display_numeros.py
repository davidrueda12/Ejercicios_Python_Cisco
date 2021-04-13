# Ejercicio que imprime cualquier numero en display de siete segmentos.

Display = {
    '0':('###','# #','# #','# #','###'),
    '1':('  #','  #','  #','  #','  #'),
    '2':('###','  #','###','#  ','###'),
    '3':('###','  #','###','  #','###'),
    '4':('# #','# #','###','  #','  #'),
    '5':('###','#  ','###','  #','###'),
    '6':('###','#  ','###','# #','###'),
    '7':('###','  #','  #','  #','  #'),
    '8':('###','# #','###','# #','###'),
    '9':('###','# #','###','  #','###')
}

while True:
    try:
        numero = str(input("Digite un numero: "))
        assert numero.isdigit()==True
        for j in range(len(Display["9"])):
            print(" ".join(Display[i][j] for i in numero))
        break

    except AssertionError:
        print("Por favor digite solo numeros positivos, usted digito es {}".format(numero))
    except KeyboardInterrupt: 
        print("Proceso interrumpido")
        break
        

