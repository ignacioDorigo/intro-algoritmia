# TP 4
# Ejercicio 4
# Desarrollar un programa que imprima
# la suma de los números impares comprendidos entre 42 y 176.

suma = 0
for i in range(42,176):
    if (i%2!=0):
        suma = suma + i

print(f"Suma de Impares desde 42 hasta 176: {suma}")