# TP 3
# Ejercicio 8
# Leer tres números correspondientes al
# día, mes y año de una fecha
# e imprimir un mensaje indicando si la fecha es válida o no.
# No hace falta hacer validacion del anio bisiesto
# Suponer que febrero tiene 28 dias
dia=int(input("Dia --> "))
mes=int(input("Mes --> "))
anio=int(input("Anio --> "))

if (mes<=0 or mes>=13):
    print("ERROR: Mes inexistente")
    
elif (dia<=0 or dia>=32):
    print("ERROR: Cantidad de dias inexistente")
    
else:
    # Mes con 28 dias
    if (mes == 2):
        if(dia <= 28):
            print("Fecha valida: ",dia,"/",mes,"/",anio)
        else:
            print("Febrero solo tiene 28 dias")
            print("ERROR: Fecha INVALIDA: ",dia,"/",mes,"/",anio)
    # Meses con 31 dias
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 9 or mes == 10 or mes == 12):
            if(dia <= 31):
                print("Fecha valida: ",dia,"/",mes,"/",anio)
            else:
                print("Este mes solo tiene 31 dias")
                print("ERROR: Fecha INVALIDA: ",dia,"/",mes,"/",anio)
    else:
        # Meses con 30 dias
        if(dia <= 30):
            print("Fecha valida: ",dia,"/",mes,"/",anio)
        else:
            print("Este mes solo tiene 30 dias")
            print("ERROR: Fecha INVALIDA: ",dia,"/",mes,"/",anio)
    