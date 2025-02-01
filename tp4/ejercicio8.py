# TP 4
# Ejercicio 8
# Ingresar números, hasta que la suma
# de los números pares supere 100.
# Mostrar cuántos números se ingresaron en total.

cont = 0
n = 0
suma = 0
while suma <= 100:
    n = int(input("Ingrese un numero: "))
    suma = suma + n
    cont = cont + 1

print(f"CANTIDAD DE NUMEROS INGRESADOS : {cont}")
print(f"SUMA FINAL: {suma}")
