#TP 2
# Estructura Secuencial
# Ejercicio 11
# Un banco necesita para sus cajeros automáticos
# un programa que lea una cantidad de dinero e
# imprima a cuántos billetes equivale
# considerando que existen billetes de $1000, $500, $100, $50 y $10.
# Desarrollar dicho programa de tal forma que
# se minimice la cantidad de billetes entregados por el cajero.
# Mostrar un mensaje de error si no se pudiera entregar la cantidad solicitada.

dineroRetirar = int(input("Ingrese cuanto quiere retirar --> "))
dineroR = dineroRetirar
b1000 = dineroRetirar // 1000
dineroRetirar = dineroRetirar % 1000

b500 = dineroRetirar // 500
dineroRetirar = dineroRetirar % 500

b100 = dineroRetirar // 100
dineroRetirar = dineroRetirar % 100

b50 = dineroRetirar // 50
dineroRetirar = dineroRetirar % 50

b10 = dineroRetirar // 10
dineroRetirar = dineroRetirar % 10

if (dineroRetirar>0):
    print("No te puedo dar la cantidad solicitada xq no tengo billetes de menor denominacion")
else:
    print(b1000,"Billetes de $1000")
    print(b500,"Billetes de $500")
    print(b100,"Billetes de $100")
    print(b50,"Billetes de $50")
    print(b10,"Billetes de $10")
        