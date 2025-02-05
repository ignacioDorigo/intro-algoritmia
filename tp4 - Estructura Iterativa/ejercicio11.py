# TP 4
# Ejercicio 10
# Realizar un programa que...
# lea un numero natural H , y
# verifique si es primo o no

divisores = 0
h = int(input("Ingrese numero para averiguar si es primo --> "))
for i in range(1,h+1):
    if (h%i==0):
        divisores = divisores + 1

if (divisores==2):
    print(f"{h} es primo")
else:
    print(f"{h} NO es primo")
    