# # TP 5
# # Ejercicio 3
# # Una empresa aplica el siguiente procedimiento
# # en la comercialización de sus productos:
# # Aplica el precio base a la primera docena de unidades.
# # Aplica un 10% de descuento a todas las unidades entre 13 y 100.
# # Aplica un 25% de descuento a todas las unidades por encima de las 100.
# # Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100.
# # El cálculo resultante sería:
# #		100 * 12 + 90 * 88 + 75 * 130 = 18870
# # y el precio promedio es de 18870/230 = 82.04

# Escribir un programa que lea la cantidad
# solicitada de un producto y su precio base,
# y muestre el valor total de la venta y el precio promedio por unidad.
# El fin de carga se determina ingresando -1 como cantidad solicitada.
# Al finalizar informar:
# Cantidad de ventas realizadas total.
# Cantidad de ventas en las que se aplicó un 10% de descuento.
# Cantidad de ventas en las que SOLO se aplicó el precio base,
# es decir que no se le realizaron descuentos.

cantidadUnidades = int(input("Ingrese cantidad de unidades: "))
ventasTotales = 0
ventas10 = 0
ventasSinDesc = 0
while (cantidadUnidades != -1):
    precioBase = float(input("Ingrese precio base "))
    while (precioBase<=0):
        print("ERROR: PRECIO INVALIDO")
        precioBase = float(input("Ingrese precio base "))
    
    unidades = cantidadUnidades
    precioFinal = 0
    if (unidades <= 12):
        precioFinal = unidades * precioBase
        ventasSinDesc = ventasSinDesc + 1
        
    elif (unidades <= 100):
        precioFinal = (12 * precioBase) + ((unidades-12)* (precioBase*.9))
        ventas10 = ventas10 + 1
    
    else:
        precioFinal = (12 * precioBase) + ((88)* (precioBase*.9)) + ((unidades-100)*(precioBase*.75))
    
    precioPromedio = precioFinal / cantidadUnidades

    ventasTotales = ventasTotales + 1
    print(f"PRECIO FINAL {precioFinal}")
    print(f"PRECIO UNITARIO PROMEDIO : {precioPromedio}")
    cantidadUnidades = int(input("Ingrese cantidad de unidades: "))

print(f"VENTAS TOTALES: {ventasTotales}")
print(f"VENTAS CON 10% DESC: {ventas10}")
print(f"VENTAS CON 0% DESC: {ventasSinDesc}")