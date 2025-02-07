# TP 6
# EJERCICIO 6
# Escribir la función comparar(a, b)
# que reciba como parámetros dos números enteros
# y devuelva
# --> 1 si el primero es mayor que el segundo
# --> 0 si son iguales
# --> -1 si el primero es menor que el segundo.
# En este ejercicio debe aprovecharse la función del ejercicio anterior.
# Ejemplo: comparar(4, 2) devuelve 1, y comparar (2, 4) devuelve -1.

def comparar(primero, segundo):
    if (primero > segundo):
        return 1
    
    elif(primero < segundo):
        return -1
    
    else:
        return 0
    
prim = int(input("INGRESE UN NUMERO --> "))
seg = int(input("INGRESE OTRO NUMERO --> "))
resultado = comparar(prim,seg)
print(f"{resultado}" )