# TP 5
# Ejercicio 9
# Ingresar un número N y validar que sea positivo.
# Luego: Mostrar los primeros números impares, hasta alcanzar el número ingresado.
# Informar la suma de esos números impares.
# Ejemplo:

# Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.

# Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.

# Si se ingresa -5, se debe pedir otro número.

n = int(input("INGRESAR NUMERO ---> "))
while (n<0):
    print(f"EL NUMERO DEBE SER POSITIVO")
    n = int(input("INGRESAR NUMERO ---> "))

sumaImpares = 0
for i in range(1,n+1,2):
    sumaImpares = sumaImpares + i
    print(i,end=" ")
    
print(sumaImpares)
print()