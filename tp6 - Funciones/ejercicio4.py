# TP 6
# EJERCICIO 4
# Devolver True si el número entero
# recibido como primer parámetro
# es multiplo del segundo, o False en caso contrario.
# Ejemplo: esmultiplo(40, 8) devuelve True y
# esmultiplo(50, 3) devuelve False.

def esMultiplo(num1,num2):
    if(num1 % num2 == 0):
        return True
    else:
        return False
    
numero1 = int(input("NUMERO 1 ---> "))
numero2 = int(input("NUMERO 2 ---> "))
resultado = esMultiplo(numero1,numero2)
print(resultado)
    