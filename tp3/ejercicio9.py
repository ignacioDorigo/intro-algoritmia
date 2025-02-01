# TP 3
# Ejercicio 9
# Diseñar un programa que calcule y
# muestre el sueldo neto de un empleado en base a
# su sueldo básico y su antigüedad en años.
# Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad
# mientras que si es casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
# También se le realizan los siguientes descuentos:
# Jubilación: 11%
# Obra Social: 3%
# Sindicato: 3%
# Como datos de entrada se ingresa por teclado el sueldo básico,
# antigüedad y estado civil (1 si es soltero o 2 si es casado).

# 1 Soltero, 2 Casado
sueldoBasico = float(input("Ingrese su sueldo básico: "))
antiguedad = int(input("Cuantos años trabajaste? "))
estadoCivil = int(input("1 --> Soltero    2 --> Casado "))
if (antiguedad<0):
    print("Tu antiguedad no puede ser negativa")
    
elif (sueldoBasico<0):
    print("Tu sueldo basico no puede ser negativo")
    
elif (estadoCivil <1 or estadoCivil>2):
    print("Ingresaste estado civil erroneo")

else:
    incremento = 0
    if (estadoCivil == 1):
        incremento = sueldoBasico * 0.05 * antiguedad
        
    elif (estadoCivil == 2):
        incremento = sueldoBasico * 0.07 * antiguedad
    
    jubilacion = (sueldoBasico + incremento) * 0.11
    obraSocial = (sueldoBasico + incremento - jubilacion) * 0.03
    sindicato = (sueldoBasico + incremento - jubilacion - obraSocial) * 0.03

    print("Sueldo Basico : ",sueldoBasico)
    print("Antiguedad  : +",incremento)
    print("Jubilacion: -",jubilacion)
    print("Obra Social: -",obraSocial)
    print("Sindicato: -",sindicato)
    
    



