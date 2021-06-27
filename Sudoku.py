# Lee el tablero de sudoku
def leer():
  A = []
  for i in range(9):
    try:
        linea = input()
        assert linea.replace(" ","").isalnum() == True
        A.append(list(linea))
    except AssertionError:
        print("Por favor digite solo cadenas,usted digito {}".format(linea))
  return A

# Imprime el tablero de sudoku
def imprimir(A):
  for i in range(len(A)):
    if i%3==0:#lee las filas y determina donde marcar
      print('+---+---+---+')
    for j in range(len(A[i])):#lee las columnas y determina donde marcar
      if j%3==0:
        print('|',end='')
      if A[i][j]!='0':
        print(A[i][j],end='')
      else:
        print(' ',end='')
    print('|')
  print('+---+---+---+')

# Encuentra la primer casilla vacia de arriba a abajo, izquierda a derecha
def casilla_vacia(A):
  for i in range(9):
    for j in range(9):
      if A[i][j] == '0':
        return (i,j)
  return None

# Mira la fila para ver si es posible o no poner el número k en la casilla i,j 
def valido_en_fila(A, i, j, k):
  for m in range(9):
    if A[i][m] == k:
      return False
  return True

# Mira la columna para ver si es posible o no poner el número k en la casilla i,j 
def valido_en_columna(A, i, j, k):
  for m in range(9):
    if A[m][j] == k:
      return False
  return True

# Mira el recuadro para ver si es posible o no poner el número k en la casilla i,j 
def valido_en_celda(A, i, j , k):
  celda_fila = 3*(i//3)
  celda_columna = 3*(j//3)
  for n in range(celda_fila,celda_fila+3):
    for m in range(celda_columna,celda_columna+3):
      if A[n][m] == k:
        return False
  return True

# Mira si es posible poner el número k en la casilla i,j
def valido(A,i,j,k):
  return valido_en_fila(A,i,j,k) and valido_en_columna(A,i,j,k) and valido_en_celda(A,i,j,k)

# Soluciona el sudoku
def solucionar(A):
  x = casilla_vacia(A)
  if x!=None:
    i,j = x
    for k in range(1,10):
      v = str(k)
      if valido(A,i,j,v):
        A[i][j] = v
        solucionar(A)
        if casilla_vacia(A)==None:
          return A
        else:
          A[i][j] = '0'
  return A

# Programa principal
print("Bienvenido a SUDOKU 9X9!\nPorfavor digite 9 numeros por fila sin espacios, si el espacio del sudoku esta vacion poner un 0")
imprimir(solucionar(leer()))
