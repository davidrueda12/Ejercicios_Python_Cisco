#Ejemplos de listas bidimensionales y busqueda de datos dentro de esta:

temps = [[0.0 for h in range (24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

mas_alta = -100.0

for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp

print("La temperatura más alta fue:", mas_alta)

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# la matriz se actualiza mágicamente aquí
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, " fueron los días calurosos.")

#Ejemplo de listas tridimensionales

habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#habitaciones ocupadas y desocupadas
habitaciones[1][9][13] = True 
habitaciones[0][4][1] = False 
#Verifica si una habitacion esta ocupada o no
vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1