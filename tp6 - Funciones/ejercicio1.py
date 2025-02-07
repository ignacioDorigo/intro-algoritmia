# TP 5
# EJERCICIO 1
# Escribir una función que reciba como parámetros dos números enteros.
# Calcular y devolver el resultado de la multiplicación de ambos
# valores utilizando solamente sumas.
# Por ejemplo 4 * 3 = 4 + 4 +4.

def multiplicacion(a,b):
    suma = 0
    for i in range(b):
        suma = suma + a
    
    return suma


a = int(input("INGRESE NUMERO ---> "))
b = int(input("INGRESE NUMERO ---> "))
resultado = multiplicacion(a,b)
print(f"EL RESULTADO DE {a} * {b} ES {resultado}")
