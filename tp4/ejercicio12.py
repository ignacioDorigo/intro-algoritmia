# TP 4
# Ejercicio 12
# La sucesión de Fibonacci es una sucesión
# de números enteros donde cada término se
# obtiene como suma de los dos anteriores,
# siendo los dos primeros 0 y 1.
# Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21
# Realizar un programa que lea N
# e imprima los N primeros términos de esta sucesión
# como así también la suma de los mismos.


n = int(input("Ingrese un numero para calcular su fib: "))
fibonacci1 = 0
fibonacci2 = 1
for i in range(n+1):
    if(i == 0):
        print(fibonacci1)
        
    elif(i==1):
        print(fibonacci2)
    
    else:
        print(fibonacci1 + fibonacci2)
        aux = fibonacci1
        fibonacci1 = fibonacci2
        fibonacci2 = fibonacci2 + aux

    