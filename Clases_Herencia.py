import time

#issubclass(ClaseUno, ClaseDos): verificar si una clase particular es una subclase de cualquier otra clase.
#isinstance(nombreObjeto, nombreClase): La función devuelve True si el objeto es una instancia de la clase o de alguna superclase.
#is: Verifica si dos variables (en este caso objetoUno y objetoDos) se refieren al mismo objeto.

#Herencia de propiedades y metodos:
class Super:
    supVar = 1

    def __init__(self, nombre):
        self.nombre = nombre
        self.supVar1 = 11

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    subVar = 2

    def __init__(self, nombre):
        Super.__init__(self, nombre) # Or super().__init__(nombre)
        self.subVar1 = 12


obj = Sub("Andy")

print(obj)
print(obj.subVar)
print(obj.supVar)
print(obj.subVar1)# No se hereda si no es llamado el constructor de la clase Super en sub
print(obj.supVar1)

# Herencias multiples

class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB): #Obtiene los metodos y propiedades de ambas super clases.
    pass

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())

# Herencias multiples:
class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"


class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"

class Sub(Izquierda, Derecha): #Si los atributos o metodos se repiten en ambas superclases
                               # python reconocera solo los de la primera suplerclase mencionada 
    pass


obj = Sub()

print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())

# Ejemplo de jerarquia de clases:

class Vehiculo:
    def cambiardireccion(izquierda, on): #Metodo abstracto (demuestra alguna posibilidad que de instanciara mas tarde)
        pass

    def girar(izquierda):
        cambiardireccion(izquierda, True)
        time.sleep(0.25)
        cambiardireccion(izquierda, False)

class VehiculoOruga(Vehiculo):
    def control_de_pista(izquierda, alto):
        pass

    def cambiardireccion(izquierda, on):
        control_de_pista(izquierda, on)

class VehiculoTerrestre(Vehiculo):
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def cambiardireccion(izquierda, on):
        girar_ruedas_delanteras(izquierda, on)

# Composición: Es el proceso de componer un objeto usando otros objetos diferentes
# Ejemplo de composicion: 

class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)