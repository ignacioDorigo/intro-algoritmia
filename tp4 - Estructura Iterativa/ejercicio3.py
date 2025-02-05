# TP 4
# Ejercicio 3
# Realizar un programa para ingresar desde el
# teclado un conjunto de números y mostrar por
# pantalla el menor y el mayor de ellos.
# Finalizar la lectura de datos con un valor -1.

numero = int(input("Ingrese un numero: "))
mayor = -9999
menor = 9999
while (numero!=-1):
    if(numero>mayor):
        mayor = numero
    if (numero<menor):
        menor = numero
    numero = int(input("Ingrese un numero: "))
    
print(f"MAYOR: {mayor}")
print(f"MENOR: {menor}")
