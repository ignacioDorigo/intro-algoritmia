#TP 2
# Estructura Secuencial
# Ejercicio 10
# Leer un período en segundos
# e imprimirlo expresado en días, horas, minutos y segundos.
# Por ejemplo, 200000 segundos equivalen a 2 días,
# 7 horas, 33 minutos y 20 segundos.

segundos = int(input("Ingrese segundos -->"))
segundosIniciales = segundos
dias = segundos // (24*60*60)
segundos = segundos % (24*60*60)
horas = segundos // (60*60)
segundos = segundos % (60*60)
minutos = segundos // 60
segundos = segundos % 60

print(segundosIniciales," segundos son: ")
print("Dias:",dias)
print("Horas:",horas)
print("Minutos:",minutos)
print("Segundos:",segundos)