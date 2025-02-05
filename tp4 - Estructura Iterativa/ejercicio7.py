# TP 4
# Ejercicio 7
# Leer 10 números enteros
# e imprimir su promedio,
# el mayor valor leído
# y en qué posición se encontraba.
# Si se ingresó más de una vez debe informar la primera.

suma = 0
mayor = -9999
posMayor = 0
for i in range(10):
    n = int(input("Ingrese un numero: "))
    suma = suma + n
    if(n>mayor):
        mayor = n
        posMayor = i + 1
    
promedio = suma / 10
print(f"PROMEDIO: {promedio}")
print(f"MAYOR: {mayor}")
print(f"POSICION MAYOR: {posMayor}")
    