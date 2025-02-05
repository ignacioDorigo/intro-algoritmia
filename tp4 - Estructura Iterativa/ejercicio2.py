# TP 4
# Ejercicio 2
# Realizar un programa para ingresar desde el teclado
# un conjunto de números e informar si
# la cantidad de elementos es impar o par, sin utilizar contadores.
# Finalizar la lectura de datos con el valor -1

par = True
numero = int(input("Ingrese un numero (-1 para terminar): "))
while numero != -1 :
    if(par):
        par = False
    else:
        par = True
    numero = int(input("Ingrese un numero (-1 para terminar): "))
    
if(par):
    print("Ingresaste una cantidad PAR de numeros")
else:
    print("Ingresaste una cantidad IMPAR de numeros")