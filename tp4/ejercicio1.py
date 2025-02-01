# TP 4
# Ejercicio 1
# Realizar un programa para ingresar desde el teclado un conjunto de números.
# Al finalizar mostrar por pantalla el primer y último elemento ingresado.
# Finalizar la lectura con el valor -1.

primero = -1
ultimo = -1
numero = int(input("Ingrese un numero (-1 para terminar): "))
primero = numero
while numero != -1 :
    ultimo = numero
    numero = int(input("Ingrese un numero (-1 para terminar): "))

print("Primero: ",primero)
print("Ultimo: ",ultimo)
    

    