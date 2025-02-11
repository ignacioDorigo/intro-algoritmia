# TP 6
# EJERCICIO 11
# Obtener el dígito central de un número entero pasado como parámetro
# sólo si la cantidad de dígitos es impar.
# Si la longitud fuera par devolver -1.
# Ejemplo: digitocentral(12345) devuelve 3
# y digitocentral(123456) devuelve -1.

def cantDigitos(numero):
    cont = 1
    while(numero>9):
        cont = cont + 1
        numero = numero // 10
    
    return cont


def digitoCentral(numero):
    cantidadDigitos = cantDigitos(numero)
    if(cantidadDigitos%2 == 0):
        return -1
    elif(cantidadDigitos == 1):
        return numero
    else:
        mitad = cantidadDigitos // 2 + 1
        central = 0
        for i in range(mitad):
            central = numero % 10
            numero = numero // 10
            
        return central
        
        

a = int(input("INGRESE UN NUMERO --> "))
central = digitoCentral(a)
print(f"El Digito Central de {a} es {central}")
