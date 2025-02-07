# TP 6
# EJERCICIO 5
#  Desarrollar la función signo(n)
# que reciba un número entero y devuelva
#  1 (positivo)
# -1 (negativo)
#  0 (nulo)

def signo(n):
    if (n<0):
        return -1
    
    elif (n>0):
        return 1
    
    else:
        return 0
    
numero = int(input("NUMERO --> "))
resultado = signo(numero)
print(f"SIGNO --> {resultado}")