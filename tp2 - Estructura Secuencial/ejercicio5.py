#TP 2
# Estructura Secuencial
# Ejercicio 5
# Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales)
# Calcular que porcentaje invirtio cada


juan = float(input("Cuanta plata invirtio Juan? --> "))
pepe = float(input("Cuanta plata invirtio Pepe? --> "))
tito = float(input("Cuanta plata invirtio Tito? --> "))

todo = juan + pepe + tito
porcentajeJuan = juan * 100 / todo
porcentajePepe = pepe * 100 / todo
porcentajeTito = tito * 100 / todo

print("Juan tiene un ",porcentajeJuan,"%")
print("Pepe tiene un ",porcentajePepe,"%")
print("Tito tiene un ",porcentajeTito,"%")