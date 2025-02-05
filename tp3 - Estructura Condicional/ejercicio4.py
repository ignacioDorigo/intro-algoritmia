# TP 3
# Ejercicio 4
# Ingresar las notas de los dos parciales de un alumno
# e indicar si promocionó, probó o si debe recuperar.
# Informar un error si el valor de alguna nota no está entre 0 y 10.
# --> Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
# --> Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
# --> Se debe recuperar cuando al menos una de las dos notas es menor a 4.

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
if(nota1<0 or nota1>10):
    print("La nota1 no es valida")
    
elif(nota2<0 or nota2>10):
    print("La nota2 no es valida")
    
else:
    if (nota1>=7 and nota2>=7):
        print("Promocionaste")
    
    elif (nota1>=4 and nota2>=4):
        print("Aprobaste")

    else:
        if(nota1<4):
            print("Debes recuperar la nota1")
        else:
            print("Debes recuperar la nota2")