# TP 5
# Ejercicio 6
# Leer un número entero y
# mostrar un mensaje informando cuántos dígitos contiene.
# Tener en cuenta que el número puede ser negativo.
# Ejemplo: Si se ingresa 12345 se debe imprimir 5.

numero = int(input("Ingrese un numero --> "))
if(numero < 0):
    numero = numero * -1
print(f"NUMERO: {numero}")
digitos = 1
while (numero>9):
    digitos = digitos + 1
    numero = numero // 10
print(f"DIGITOS: {digitos}")
