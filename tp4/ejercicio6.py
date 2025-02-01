# TP 4
# Ejercicio 6
# Mostrar la tabla de multiplicar (entre 1 y 12) del número 4.
# ¿Cómo cambiaría el algoritmo para
# que el usuario pueda decidir la tabla de multiplicar a mostrar?

numTabla = int(input("Ingrese un numero: "))
for i in range(1,12+1):
    resultado = numTabla * i
    print(f"{numTabla} * {i} = {resultado}")