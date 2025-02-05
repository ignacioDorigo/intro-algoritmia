# TP 3
# Ejercicio 6
# Una remisería requiere un programa que calcule el precio de un viaje
# a partir de la cantidad de kilómetros que desea recorrer el usuario.
# Para eso cuenta con la siguiente tarifa:
# Viaje mínimo $150
# Si recorre entre 0 y 10 km: $20 por km
# Si recorre 10 km o más: $15 por km

km = int(input("Ingrese cuantos km quiere recorrer: "))
bandera = 150
if (km>=0 and km<=10):
    precio = bandera + (20*km)
    print("Precio: $",precio)
    
elif(km>=15):
    precio = bandera + (15 * km)
    print("Precio: $",precio)