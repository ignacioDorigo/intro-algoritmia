#TP 2
# Estructura Secuencial
# Ejercicio 9
# Una inmobiliaria paga a sus vendedores un salario de $50000,
# más una comisión de $5000 por cada venta realizada,
# más el 5% del valor de las ventas.
# Realizar un programa que
# imprima el número del vendedor y el salario que le corresponde en un determinado mes.
# Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

numeroVendedor = int(input("Ingrese su numero de vendedor --> "))
cantidadVentas = int(input("Cuantas ventas hizo? --> "))
valorTotalVentas = float(input("Monto total de las ventas hizo? --> "))

sueldoBase = 50000
comisionCantidadVentas = 5000 * cantidadVentas
comisionValorVentas = valorTotalVentas * 0.05

sueldoFinal = sueldoBase + comisionCantidadVentas + comisionValorVentas
print("Vendedor: ",numeroVendedor,)
print("Salario final: $",sueldoFinal)