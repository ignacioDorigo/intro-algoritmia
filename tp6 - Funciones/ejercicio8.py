# TP 5
# EJERCICIO 8
# La raíz cuadrada de un número positivo n
# puede calcularse mediante la siguiente
# fórmula de Newton: 0 2
# donde a es una aproximación a n.
# Al aplicar repetidamente esta
# fórmula reemplazando a por la
# aproximación obtenida en el paso anterior
# se obtiene cada vez una aproximación mejor.
# Desarrollar un programa que calcule la raíz
# cuadrada aproximada de un número entero
# positivo n utilizando como primera aproximación a n/2.
# Detener el proceso cuando la diferencia entre
# dos cálculos sucesivos sea menor a 0,0001.

n = int(input("INGRESE NUMERO PARA CALCULAR RAIZ CUADRADA --> "))
while (n<0):
    print("ERROR NO SE PUEDE CALCULAR RAIZ DE UN NEGATIVO")
    n = int(input("INGRESE NUMERO PARA CALCULAR RAIZ CUADRADA --> "))

a = (n/2)
raiz = ((n/a) + a) / 2

while (a-raiz) > 0.0001:
    a = raiz
    raiz = ((n/a) + a) / 2

print(f"RAIZ DE {n} es {raiz}")
