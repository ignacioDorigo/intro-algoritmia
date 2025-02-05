# TP 5
# Ejercicio 2
# Escribir un programa que permita ingresar los números de legajo
# de los alumnos de un curso y su nota de examen final.
# El fin de la carga se determina ingresando un -1 en el legajo.
# Informar para cada alumno si aprobó o no el examen
# considerando que se aprueba con nota mayor o igual a 4.
# Se debe validar que la nota ingresada sea entre 1 y 10.
# Terminada la carga de datos, informar:
# Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
# Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
# Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

legajo = int(input("Ingrese legajo ---> "))
aplazados = 0
desaprobados = 0
aprobados = 0
while (legajo != -1):
    nota = int(input("Ingrese nota (entre 1 y 10)--->: "))
    while (nota<1 or nota>10):
        print("ERROR: INGRESE NOTA VALIDA")
        nota = int(input("Ingrese nota (entre 1 y 10)--->: "))
    if(nota>=4):
        print("Aprobaste")
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1
        if(nota>1):
            print("Desaprobaste")

        else:
            print("Desaprobaste y Te Aplazaron")
            aplazados = aplazados + 1
    
    print()
    legajo = int(input("Ingrese legajo (-1 PARA TERMINAR)---> "))
    
print(f"APROBADOS : {aprobados}")
print(f"DESAPROBADOS : {desaprobados}")
porcentajeAplazados = 0
if ((desaprobados + aprobados)>0):
    porcentajeAplazados = aplazados * 100 / (desaprobados + aprobados)
print(f"% APLAZADOS : {porcentajeAplazados}%")
