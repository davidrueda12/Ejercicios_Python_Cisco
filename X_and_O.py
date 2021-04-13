# Tic Tac Toe
 
import random
 
def dibujarTablero(tablero):
    # Esta funcion dibuja el tablero en el que se jugara
    print('+------+------+------+')
    print('|      |      |      |')
    print('| ' + tablero[7] + '    | ' + tablero[8] + '    | ' + tablero[9] + '    | ')
    print('|      |      |      |')
    print('+------+------+------+')
    print('|      |      |      |')
    print('| ' + tablero[4] + '    | ' + tablero[5] + '    | ' + tablero[6] + '    | ')
    print('|      |      |      |')
    print('+------+------+------+')
    print('|      |      |      |')
    print('| ' + tablero[1] + '    | ' + tablero[2] + '    | ' + tablero[3] + '    | ')
    print('|      |      |      |')
    print('+------+------+------+')
 
def posicionJugador():
    # El jugador elige la letra que va a usar.
    # Devuelve una lista con la letra del jugador como primer elemento y la
    # letra del computador como el segundo elemento.
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Caul escogeras la X o la O?')
        letra = input().upper()
 
    # El primer elemento en la tupla es la letra del jugador, el segundo es
    # la letra de la computadora
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def primerTurno():
    # Se escoje quien tendra el primer turno aleatoriamente.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def juegaDenuevo():
    # Esta funcion retorna verdadero si el jugador quiere volver a empezar, sino
    # retorna falso.
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')
 
def realizarMovimiento(tablero, letra, movimiento):
    tablero[movimiento] = letra
 
def Ganador(bo, le):
    # Otroga la letra y el tableo al jugador, esta funcion retorna True si
    # el jugador a ganado.

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # a traves parte superior
    (bo[4] == le and bo[5] == le and bo[6] == le) or # a traves de la parte media
    (bo[1] == le and bo[2] == le and bo[3] == le) or # a traves de la parte inferior
    (bo[7] == le and bo[4] == le and bo[1] == le) or # por el lado izquierdo
    (bo[8] == le and bo[5] == le and bo[2] == le) or # por el centro
    (bo[9] == le and bo[6] == le and bo[3] == le) or # por el lado derecho
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
 
def copiaTablero(tablero):
    # Crea un duplicado de la lista del tablero y lo retorna
    tableroDuplicado = []
 
    for i in tablero:
        tableroDuplicado.append(i)
 
    return tableroDuplicado
 
def espacioLibre(tablero, movimiento):
    # Retorna True si el movimiento esta libre en el tablero
    return tablero[movimiento] == ' '
 
def movimientoJugador(tablero):
    # El jugador escribe su movimiento.
    movimiento = ' '
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not espacioLibre(tablero, int(movimiento)):
        print('¿Cual sera tu siguiente movimiento? (1-9)')
        movimiento = input()
    return int(movimiento)
 
def escogeMovimientoAleatorioDeLista(tablero, listaMovimientos):
    # Devuelve un movimiento válido de la lista pasada en el tablero.
    # Retorna none si el movimiento no es valido.
    posiblesMovimientos = []
    for i in listaMovimientos:
        if espacioLibre(tablero, i):
            posiblesMovimientos.append(i)
 
    if len(posiblesMovimientos) != 0:
        return random.choice(posiblesMovimientos)
    else:
        return None
 
def movimientoComputadora(tablero, letraComputadora):
    # Determina a que posicion ponerse una vez definidas las letras de cada jugador y retorna el movimiento
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'
 
    # Esta parte utiliza un algoritmo de AI para el tic tac toe
    # Primero verifica si puede ganar en el siguiente movimiento
    for i in range(1, 10):
        copy = copiaTablero(tablero)
        if espacioLibre(copy, i):
            realizarMovimiento(copy, letraComputadora, i)
            if Ganador(copy, letraComputadora):
                return i
 
    # Verifica si el jugador puede ganar en el siguiente movimiento y lo bloquea
    for i in range(1, 10):
        copy = copiaTablero(tablero)
        if espacioLibre(copy, i):
            realizarMovimiento(copy, letraJugador, i)
            if Ganador(copy, letraJugador):
                return i
 
    # Intenta tomar una de las esquinas, si están libres.
    movimiento = escogeMovimientoAleatorioDeLista(tablero, [1, 3, 7, 9])
    if movimiento != None:
        return movimiento
 
    # Intanta tomar el centro si esta libre.
    if espacioLibre(tablero, 5):
        return 5
 
    # Se mueve por uno de los lados
    return escogeMovimientoAleatorioDeLista(tablero, [2, 4, 6, 8])
 
def tableroLleno(tablero):
    # Retorna True si todos los espacios del tablero estan ocupados, sino retorna False
    for i in range(1, 10):
        if espacioLibre(tablero, i):
            return False
    return True
 
 
print('¡Bienvenido a Tic Tac Toe!')
 
while True:
    # Reinicia el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = posicionJugador()
    turn = primerTurno()
    print('El ' + turn + ' comienza.')
    juengoEnDesarrollo = True
 
    while juengoEnDesarrollo:
        if turn == 'player':
            # Turno del jugador
            dibujarTablero(elTablero)
            movimiento = movimientoJugador(elTablero)
            realizarMovimiento(elTablero, letraJugador, movimiento)
 
            if Ganador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Felicidades!,¡Ganaste el juego!')
                juengoEnDesarrollo = False
            else:
                if tableroLleno(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Hubo un empate!')
                    break
                else:
                    turn = 'computer'
 
        else:
            # Turno de la computadora.
            movimiento = movimientoComputadora(elTablero, letraComputadora)
            realizarMovimiento(elTablero, letraComputadora, movimiento)
 
            if Ganador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('¡Lo lamento, la computadora te a vencido!')
                juengoEnDesarrollo = False
            else:
                if tableroLleno(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Hubo un empate!')
                    break
                else:
                    turn = 'player'
 
    if not juegaDenuevo():
        break