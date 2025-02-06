# TP 5
# Ejercicio 7
# Leer un número entero e invertir las cifras que contiene.
# Imprimir por pantalla el número invertido.
# Tener en cuenta que el número puede ser negativo.
# Por ejemplo, si se ingresa 1234 debe mostrar 4321.


numero = int(input("INGRESE NUMERO PARA INVERTIR: "))
print(f"ORIGINAL:{numero}")
if(numero < 0):
    numero = numero * -1

reves = 0
while(numero>0):
    
    ultimoDigito = numero % 10
    reves = reves * 10 + ultimoDigito
    numero = numero // 10
    print(reves)
    
print(f"INVERTIDO:{reves}")
