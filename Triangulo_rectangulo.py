#En este ejercicio verificamos si con los 3 datos digitados es posible obtener un tringulo
#Luego verificamos si este triando es rectangulo o no

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
        
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
        
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


if esUnTrianguloRectangulo(a,b,c)== False:
    print("No es un triangulo rectangulo")
else:
    print ("Es un triangulo rectangulo")

#Tambien podemos calcular el area del triagulo usando la formula de heron

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(a,b,c))