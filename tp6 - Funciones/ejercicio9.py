# TP 5
# EJERCICIO 9
# Escribir una función que reciba como parámetros
# un número de día
# un número de mes
# un número de año
# devuelva la cantidad de días que faltan hasta fin de mes.

# Luego desarrollar tres programas para:
# Ingresar una fecha formada por tres enteros (día, mes y año)
# e imprimir la cantidad de días que faltan hasta fin de año.

# Ingresar una fecha formada por tres enteros (día, mes y año)
# e imprimir la cantidad de días transcurridos
# en ese año hasta esa fecha.

# Ingresar dos fechas formadas por tres enteros (día, mes y año)
# e imprimir cuánto tiempo transcurrió entre ambas
# expresando el resultado en años, meses y días.

# Los tres programas deben realizar su trabajo a través
# de la función indicada al comienzo.

def pedirEntero(rangoMinimo,rangoMaximo,mensaje,mensajeError):
    numero = int(input(mensaje))
    while(numero<rangoMinimo or numero>rangoMaximo):
        print(mensajeError)
        numero = int(input(mensaje))
        
    return numero

        
    


def esBisiesto(ano):
    if(ano%400 == 0):
        return True
    
    elif(ano%100 == 0):
        return False
    
    elif(ano%4 == 0):
        return True
    
    else:
        return False
    
def diasMes(mes,ano):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return 31
    elif(mes == 2):
        if (esBisiesto(ano)):
            return 29
        else:
            return 28
    else:
        return 30
    
def validarFecha(dia,mes,ano):
    if(mes==2):
        if(dia<=29):
            if(dia==29):
                if(esBisiesto(ano)):
                    return True
                else:
                    return False
            else:
                return True
                
        else:
            print("FEBRERO NO TIENE MAS DE 28/29 DIAS")
            return False
        
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia <= 30):
            return True
        else:
            print("LOS MESES 4/6/9/11 NO TIENE MAS DE 30 DIAS")
            return False
    
    else:
        return True
        
            
def adelantarUnDia(dia,mes,ano):
    if(dia == 31 and mes == 12):
        dia = 1
        mes = 1
        ano = ano + 1
        
    elif(dia == 31):
        dia = 1
        mes = mes + 1
    
    elif(mes == 2):
        if(esBisiesto(ano)):
            if(dia == 29):
                dia = 1
                mes = mes + 1
            else:
                dia = dia + 1
        else:
            if(dia == 28):
                dia = 1
                mes = mes + 1
                
            else:
                dia = dia + 1
        
    elif(mes==4 or mes==6 or mes ==9 or mes==11):
        if(dia == 30):
            dia = 1
            mes = mes + 1
        else:
            dia = dia + 1
    
    else:
        dia = dia + 1
        
    
    return dia,mes,ano


def diasDesdeComienzoAno(dia,mes,ano):
    cont = 1
    d = 1
    m = 1
    a = ano
    while(d!= dia or m!=mes):
        d,m,a = adelantarUnDia(d,m,a)
        cont = cont + 1
    
    return cont
    
def diasAno(ano):
    if(esBisiesto(ano)):
        return 366
    else:
        return 365

dia = pedirEntero(1,31,"INGRESE DIA --> ","ERROR: EL DIA DEBE ESTAR ENTRE 1 y 31")
mes = pedirEntero(1,12,"INGRESE MES --> ","ERROR: EL MES DEBE ESTAR ENTRE 1 y 12")
ano = pedirEntero(-99999,999999,"INGRESE AÑO ---> ","ERROR: EL AÑO DEBE ESTAR ENTRE -99999 Y 99999")
result = validarFecha(dia,mes,ano)
print(f"RESULTADO ---> {result}")

d = dia
m = mes
a = ano
print(f"{d}/{m}/{a}")
diasTranscurridos = diasDesdeComienzoAno(d,m,a)
diasHastaFinAno = diasAno(a) - diasTranscurridos
# A
print(f"DIAS HASTA FIN DE AÑO --> {diasHastaFinAno}")
# B
print(f"DIAS DEL AÑO TRANSCURRIDOS DESDE EL 1/1/{a} --> {diasTranscurridos}")
# C
print("FALTAA ..........")

        