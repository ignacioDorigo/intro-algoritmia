# TP 6
# EJERCICIO 2
# Dados dos parámetros enteros A y B,
# obtener AB (A elevado a la B)
# mediante multiplicaciones sucesivas.
# Por ejemplo 4^3 = 4 * 4 * 4.


def potencia(base,expo):
    pot = 1
    if(expo==0):
        print(f"{base} elevado a {expo} = {pot}")
        return pot
        
    else:
        for i in range(expo):
            pot = pot * base
            
        print(f"{base} elevado a {expo} = {pot}")
        return pot


base = int(input("BASE ---> "))
expo = int(input("EXPONENTE ---> "))
resultado = potencia(base,expo)
        