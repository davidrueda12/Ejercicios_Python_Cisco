# Calcula impuestos segun el ingreso de la persona y ciertas condiciones segun el ingreso

ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso < 85528:
    impuesto = (ingreso * 0.18)-556.2
    if impuesto < 0:
        impuesto = 0
elif ingreso > 85528:
    impuesto = 14839.2 + ((ingreso-85528)*0.32)

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")