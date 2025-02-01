#TP 2
# Estructura Secuencial
# Ejercicio 7
# Una persona invierte su capital en un banco y desea saber cuanto gana en un mes
# Teniendo en cuenta que el banco paga un 2% mensual
# Cuanto ganara si deja el dinero 6 meses?

dinero = float(input("Ingrese el dinero a invertir: "))
meses = 6
interes = 2
gananciaMensual = dinero * interes / 100
gananciaFinal  = gananciaMensual * meses
print("Si dejas tu dinero en el banco vas a ganar: $",gananciaFinal)