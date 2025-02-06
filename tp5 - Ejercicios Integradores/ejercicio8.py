# TP 5
# Ejercicio 8
# Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
# Por cada empleado se lee su legajo, categoría y salario.
# Se solicita elaborar un informe que contenga:
# Importe total de salarios pagados por la empresa.
# Cantidad de empleados que ganan más de $200000.
# Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
# Legajo del empleado que más gana.
# Sueldo más bajo.
# Importe total de sueldos por cada categoría.
# Salario promedio

empleadoMas200 = 0
empleadoMas500yCat3 = 0
legajoMasGana = 0
montoMasGana = -99999
sueldoMasBajo = 0
sueldosCat1 = 0
sueldosCat2 = 0
sueldosCat3 = 0
empleados = 0


# --------------------------INICIO INGRESO DATOS ---------------------------------
legajo = int(input("LEGAJO (-1 PARA TERMINAR) ---> "))
while legajo != -1:
    empleados = empleados + 1
    categoria = int(input("CATEGORIA (1, 2 o 3) ---> "))
    while(categoria<1 or categoria>3):
        print(f"LA CATEGORIA {categoria} NO EXISTE")
        categoria = int(input("CATEGORIA (1, 2 o 3) ---> "))
    
    salario = float(input("SALARIO ---> $"))
    while(salario<0):
        print(f"EL SALARIO NO PUEDE SER NEGATIVO")
        salario = float(input("SALARIO ---> $"))
    
    if (salario>200000):
        empleadoMas200 = empleadoMas200 + 1
        
    if (salario<50000 and categoria == 3):
        empleadoMas500yCat3 = empleadoMas500yCat3 + 1
    
    if(categoria == 1):
        sueldosCat1 = sueldosCat1 + salario
        
    elif(categoria == 2):
        sueldosCat2 = sueldosCat2 + salario
        
    elif(categoria == 3):
        sueldosCat3 = sueldosCat3 + salario
    
    if(salario>montoMasGana):
        legajoMasGana = legajo
        montoMasGana = salario
    
    if(salario<sueldoMasBajo):
        sueldoMasBajo = sueldoMasBajo
    
    
    
    # ---------------------------FIN INGRESO DATOS--------------------------------
        
    legajo = int(input("LEGAJO (-1 PARA TERMINAR) ---> "))

totalSalarios = sueldosCat1 + sueldosCat2 + sueldosCat3
salarioPromedio = totalSalarios / empleados
print(f"CANTIDAD DE EMPLEADOS CON SUELDO MAYOR A 200.000: {empleadoMas200}")
print(f"CANTIDAD DE EMPLEADOS CON SUELDO MENOR A 50.000 y CAT 3: {empleadoMas500yCat3}")
print(f"SUELDOS TOTALES: {totalSalarios}")
print(f"SUELDOS CAT 1: {sueldosCat1}")
print(f"SUELDOS CAT 2: {sueldosCat2}")
print(f"SUELDOS CAT 3: {sueldosCat3}")
print(f"SUELDO MAS BAJO : {sueldoMasBajo}")
print(f"LEGAJO DEL QUE MAS GANA: {legajoMasGana} CON ${montoMasGana}")
print(f"SALARIO PROMEDIO: {salarioPromedio}")


