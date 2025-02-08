# TP 6
# EJERCICIO 7
# Calcular y devolver el Máximo Común Divisor
# de dos enteros no negativos
# basándose en las siguientes fórmulas matemáticas:
# MCD(X,X) = X
# MCD(XY) E MCDY, X)
# Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
# Ejemplo: MCD(40, 15) devuelve 5.
def pedirPositivo():
    numero = int(input("INGRESE NUMERO POSITIVO --> "))
    while (numero <= 0):
        print("ERROR: EL NUMERO DEBE SER POSITIVO (MAYOR A 0)")
        numero = int(input("INGRESE NUMERO POSITIVO --> "))
    
    return numero

def mcd(numero1,numero2):
    mcdMomentaneo = 1
    for i in range(1,numero1+1):
        if (numero1%i == 0 and numero2%i == 0):
            mcdMomentaneo = i
    
    return mcdMomentaneo
    

a = pedirPositivo()
b = pedirPositivo()
result = mcd(a,b)
print(f"MCD ENTRE {a} y {b} es {result}")