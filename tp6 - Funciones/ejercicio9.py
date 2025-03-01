# TP 5
# EJERCICIO 9
# Escribir una función que reciba como parámetros
# un número de día
# un número de mes
# un número de año
# PUNTO  ---> A
# devuelva la cantidad de días que faltan hasta fin de mes.

# PUNTO  ---> B
# Luego desarrollar tres programas para:
# Ingresar una fecha formada por tres enteros (día, mes y año)
# e imprimir la cantidad de días que faltan hasta fin de año.

# PUNTO  ---> C
# Ingresar una fecha formada por tres enteros (día, mes y año)
# e imprimir la cantidad de días transcurridos
# en ese año hasta esa fecha.

# PUNTO  ---> D
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
    
def diasHastaFinMes(dia,mes,ano):
    diasDelMes = diasMes(mes,ano)
    return (diasDelMes - dia)
    
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
    

def diasDesdeF1hastaF2(d1,m1,a1,d2,m2,a2):
    diaMayor = 0
    mesMayor = 0
    anoMayor = 0
    diaMenor = 0
    mesMenor = 0
    anoMenor = 0
    if (a1>a2):
        diaMayor = d1
        mesMayor = m1
        anoMayor = a1
        diaMenor = d2
        mesMenor = m2
        anoMenor = a2
    elif (a2>a1):
        diaMayor = d2
        mesMayor = m2
        anoMayor = a2
        diaMenor = d1
        mesMenor = m1
        anoMenor = a1
    else:
        if(m1>m2):
            diaMayor = d1
            mesMayor = m1
            anoMayor = a1
            diaMenor = d2
            mesMenor = m2
            anoMenor = a2
            
        elif(m2>m1):
            diaMayor = d2
            mesMayor = m2
            anoMayor = a2
            diaMenor = d1
            mesMenor = m1
            anoMenor = a1
        
        else:
            if(d1>d2):
                diaMayor = d1
                mesMayor = m1
                anoMayor = a1
                diaMenor = d2
                mesMenor = m2
                anoMenor = a2
                
            elif(d2>d1):
                diaMayor = d2
                mesMayor = m2
                anoMayor = a2
                diaMenor = d1
                mesMenor = m1
                anoMenor = a1
                
            else:
                return 0
    dias = 0
    while (diaMenor!=diaMayor or mesMenor!=mesMayor or anoMenor!=anoMayor):
        diaMenor,mesMenor,anoMenor = adelantarUnDia(diaMenor,mesMenor,anoMenor)
        dias = dias + 1
    
    return dias
            

dia = pedirEntero(1,31,"INGRESE DIA --> ","ERROR: EL DIA DEBE ESTAR ENTRE 1 y 31")
mes = pedirEntero(1,12,"INGRESE MES --> ","ERROR: EL MES DEBE ESTAR ENTRE 1 y 12")
ano = pedirEntero(-99999,999999,"INGRESE AÑO ---> ","ERROR: EL AÑO DEBE ESTAR ENTRE -99999 Y 99999")
# result = validarFecha(dia,mes,ano)
# print(f"RESULTADO ---> {result}")

d = dia
m = mes
a = ano

print(f"FECHA 1 ---> {d}/{m}/{a}")
print()


# A
print("PUNTO 1 --> DIAS HASTA FIN DE MES")
print(f"DIAS HASTA FIN DE MES {diasHastaFinMes(d,m,a)}")
print()

# B
print("PUNTO 2 --> DIAS HASTA FIN DE ANO ")
diasTranscurridos = diasDesdeComienzoAno(d,m,a)
diasHastaFinAno = diasAno(a) - diasTranscurridos
print(f"DIAS HASTA FIN DE AÑO --> {diasHastaFinAno}")
print()

# C
print("PUNTO 3 --> DIAS DEL ANO TRANSCURRIDOS")
print(f"DIAS DEL AÑO TRANSCURRIDOS DESDE EL 1/1/{a} --> {diasTranscurridos}")
print()

# D
print("PUNTO 3 --> DIAS DEL ANO TRANSCURRIDOS")
dia2 = pedirEntero(1,31,"INGRESE DIA --> ","ERROR: EL DIA DEBE ESTAR ENTRE 1 y 31")
mes2 = pedirEntero(1,12,"INGRESE MES --> ","ERROR: EL MES DEBE ESTAR ENTRE 1 y 12")
ano2 = pedirEntero(-99999,999999,"INGRESE AÑO ---> ","ERROR: EL AÑO DEBE ESTAR ENTRE -99999 Y 99999")
print(f"FECHA 2 ---> {dia}/{mes2}/{ano2}")
diasDif = diasDesdeF1hastaF2(d,m,a,dia2,mes2,ano2)
anosDif = diasDif // 365
diasDif = diasDif % 365
mesesDif = diasDif // 30
diasDif = diasDif % 30
print("TIEMPO DE DIFERENCIA")
print(f"ANOS: {anosDif}")
print(f"MESES: {mesesDif}")
print(f"DIAS: {diasDif}")