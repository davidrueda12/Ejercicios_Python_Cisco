#Este ejemplo de clase nos muestra los constructores que le dan al objeto las propiedades
#de la clase

class ClaseEjemplo:
    contador = 0 #De esta forma se crea una variable de clase.
    def __init__(self, val = 1): 
        self.__primera = val #al tener __al inicio indica que es privada
        ClaseEjemplo.contador += 1 #--> Accede a la variable como cualquier atributo de la instancia

    def setSegunda(self, val):#self identifica el objeto para el cual se invoca el método.
        self.__segunda = val

objetoEjemplo1 = ClaseEjemplo() #crea el primer objeto
objetoEjemplo2 = ClaseEjemplo(2) #crea el segundo objeto dandole valor a __primera

objetoEjemplo2.setSegunda(3) #agrega valor a __segunda

objetoEjemplo3 = ClaseEjemplo(4)#crea el tercer objeto dandole valor a __primera
objetoEjemplo3.__tercera = 5 #crea una nueva propiedad en el objeto llamada __tercera


print(objetoEjemplo1.__dict__)# __dict__ permire ver las variables que el objeto tiene en forma de diccionario
print(objetoEjemplo2.__dict__)# las variables de clase no se muestran en el diccionario de un objeto y 
                              # siempre tiene el mismo valor en todas las instancias de clase
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)
print(objetoEjemplo1._ClaseEjemplo__primera) #de este modo imprime el valor de __primera siendo privado

################################################

class ClaseEjemplo1:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo1(1)
print(objetoEjemplo.a)

if hasattr(objetoEjemplo, 'b'): #esta funcion permite saber si el objeto contiene la propiedad
    print(objetoEjemplo.b)      # y returna True o False, tambien se puede usar en clases

#Atributos pre-equipados de las clases:
    #__name__: muestra el nombre de la clase, en objetos se debe usar con type
    #__module__: es una cadena, también almacena el nombre del módulo que contiene la definición de la clase.
    #__bases__: Muestra las superclases de la clase, una clase sin superclases explícitas apunta al objeto

class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia
    
    def __str__(self): #Usar __str__ permite presentar el objeto como una cadena al imprimirlo
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)