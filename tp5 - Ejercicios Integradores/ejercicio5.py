# TP 5
# Ejercicio 5
# Leer tres números D, M y A correspondientes al día, mes y año de una fecha,
# y un número entero N que representa una cantidad de días.
# Realizar un programa que imprima la nueva fecha que
# resulta de sumar N días a la fecha dada.
# Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3.

def esBisiesto(anio):
    if(anio%400 == 0):
        return True
    
    elif(anio%100 == 0):
        return False
    
    elif (anio%4==0):
        return True
    
    else:
        return False

def validarFecha(dia,mes,ano):
    print(f"{dia}/{mes}/{ano}")
    if(mes<1 or mes>12):
        print("MES INVALIDO")
        return False
    
    elif(dia<1 or dia>31):
        print("DIA INVALIDO")
        return False
    
    elif(mes==2):
        if(dia==29):
            if(esBisiesto(ano)):
                print("Fecha valida")
                return True
            else:
                print("FECHA INVALIDA: Febrero si no es bisiesto no tiene 29 dias")
                return False
    
        elif(dia<=28):
            print("Fecha Valida")
            return True
        
        else:
            print(f"FECHA INVALIDA: FEBRERO NO TIENE {dia} DIAS")
            return False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia==31):
            print("FECHA INVALIDA : El mes elegido solo tiene 30 dias")
            return False
        else:
            print("Fecha Valida")
            return True
    else:
        print("Fecha Valida")
        return True
        
def adelantarDia(dia,mes,anio):
    d=dia
    m=mes
    a=anio
    if(d==31 and m==12):
        a = a + 1
        d = 1
        m = 1
        
    elif(d==31 and (m==1 or m==3 or m == 5 or m == 7 or m==8 or m==10)):
        d = 1
        m = m + 1
        
    elif (d==30 and (m==4 or m==6 or m==9 or m==11)):
        d = 1
        m = m + 1
        
    elif (m==2 and esBisiesto(a)):
        if (d==29):
            d = 1
            m = m + 1
        else:
            d = d + 1
    elif (m==2 and esBisiesto(a)==False):
        if(d==28):
            d = 1
            m = m + 1
        else:
            d = d + 1
    else:
        d = d + 1
        
    return d,m,a
        
dia = int(input("DIA --> "))
mes = int(input("MES --> "))
ano = int(input("ANO --> "))
while(validarFecha(dia,mes,ano)==False):
    dia = int(input("DIA --> "))
    mes = int(input("MES --> "))
    ano = int(input("ANO --> "))

d = dia
m = mes
a = ano
cuantosDias = int(input("CUANTOS DIAS ADELANTAMOS: "))
print(f"FECHA INICIO: {dia}/{mes}/{ano}")
for i in range(cuantosDias):
    d,m,a = adelantarDia(d,m,a)
    print(f"{d}/{m}/{a}")



