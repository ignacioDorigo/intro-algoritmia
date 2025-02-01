# TP 4
# Ejercicio 9
# Se desea analizar cuántos autos circulan
# con patente con numeración par
# y cuántos con numeración impar en un día.
# Escribir un programa que permita ingresar
# la terminación de la patente (entre 0 y 9)
# hasta ingresar -1 e informe cuántos
# vehículos pasaron con numeración par
# y cuántos con numeración impar.

pares = 0
impares = 0
patente = int(input("Ingrese patente terminacion de patente (0 a 9) : "))
while (patente != -1):
    if(patente%2==0):
        pares = pares + 1
    else:
        impares = impares + 1
    patente = int(input("Ingrese patente terminacion de patente (0 a 9) : "))

print(f"PAR: {pares}")
print(f"IMPAR: {impares}")