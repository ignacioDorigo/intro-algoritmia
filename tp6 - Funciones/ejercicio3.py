# TP 6
# EJERCICIO 3
# Imprimir una columna de asteriscos
# donde su altura se recibe como parámetro.

cant_asteriscos = int(input("CANTIDAD DE ASTERISCOS ---> "))
while (cant_asteriscos<0):
    print("LA CANTIDAD DE ASTERISCOS NO PUEDE SER NEGATIVA")
    cant_asteriscos = int(input("CANTIDAD DE ASTERISCOS ---> "))
    
for i in range(1,cant_asteriscos+1):
    print("*"*i)