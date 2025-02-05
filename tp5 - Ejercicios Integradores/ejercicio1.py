# TP 5
# Ejercicio 1
# Leer números que representan edades de un grupo de personas
# finalizando la lectura cuando se ingrese el número -1.
# Imprimir cuántos son menores de 18 años,
# cuántos tienen 18 años o más
# y el promedio de edad de ambos grupos.
# Descartar valores que no representan una edad válida.
# (Se considera válida una edad entre 0 y 100).

edad = int(input("INGRESE EDAD --> "))
menores = 0
mayores = 0
edadMenores = 0
edadMayores = 0
while(edad!=-1):
    if (edad>=0 and edad<=100):
        if (edad<18):
            menores = menores + 1
            edadMenores = edadMenores + edad
        else:
            mayores = mayores + 1
            edadMayores = edadMayores + edad
    else:
        print("ERROR -> EDAD INVALIDA (RANGO VALIDO 0 - 100)")
    
    edad = int(input("INGRESE EDAD --> "))

promedioMayores = 0
if (mayores>0):
    promedioMayores = edadMayores // mayores
    
promedioMenores = 0
if (menores>0):
    promedioMenores = edadMenores // menores
    
print(f"MAYORES: {mayores} personas y su promedio de edad es {promedioMayores}")
print(f"MENORES: {menores} personas y su promedio de edad es {promedioMenores}")