# TP 3
# Ejercicio 3
# Ingresar el numero de mes y mostrar el nombre del mes correspondiente
# Ejemplo: Si el usuario ingresa 4, entonces se muestra "Abril"
# En caso de no existir el mes, informar mensaje de error

mes = int(input("Ingrese el numero de mes: "))
if(mes<=0 or mes>=13):
    print("ERROR: El mes que ingresaste no existe")
    
elif(mes == 1):
    print("Enero")

elif(mes == 2):
    print("Febrero")

elif(mes == 3):
    print("Marzo")
    1
elif(mes == 4):
    print("Abril")
    
elif(mes == 5):
    print("Mayo")
    
elif(mes == 6):
    print("Junio")
    
elif(mes == 7):
    print("Julio")
    
elif(mes == 8):
    print("Agosto")
    
elif(mes == 9):
    print("Septiembre")
    
elif(mes == 10):
    print("Octubre")
    
elif(mes == 11):
    print("Noviembre")
    
elif(mes == 12):
    print("Diciembre")