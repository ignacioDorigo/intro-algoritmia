# TP 5
# EJERCICIO 10
# Extraer un dígito de un número.
# La función recibe como parámetros dos números enteros
# --> uno será del que se extraiga el dígito
# --> el otro indica qué cifra se desea obtener.
# La cifra de la derecha se considera la número 0.
# Retornar el valor -1 si no existe el dígito solicitado.
# Tener en cuenta que el número puede ser positivo o negativo.
# Ejemplo: extraerdigito(12345, 1) devuelve 4,
# y extraerdigito(12345, 8) devuelve -1.

def extraerDigito(numero,digito):
    if (numero<0):
        numero = numero * -1
        
    posicion = 0
    encontrado = False
    while(numero>0):
        print(numero)
        ultimoDerecha = numero % 10
        if(ultimoDerecha == digito):
            encontrado = True
            break
        
        numero = numero // 10
        posicion = posicion + 1
    
    if (encontrado == True):
        return posicion
    else:
        return -1
    

entero = int(input("Ingrese un numero --> "))
digit = int(input("Ingrese digito a extraer --> "))
result = extraerDigito(entero,digit)
print(f"RESULTADO --> {result}")
        