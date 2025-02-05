# TP 5
# Ejercicio 4
# Una empresa factura a sus clientes el último día de cada mes.
# Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, tiene un
# descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente.
# Si paga en los siguientes 10 días del mes deberá
# pagar el importe original de la factura
# mientras que si paga después del día 20
# deberá abonar una multa de $350 o del 10% de su factura,
# lo que resulte mayor.
# Escribir un programa que lea el número del cliente y
# el total de la factura, y emita un informe donde
# conste el número del cliente y
# los tres importes que podría abonar según la fecha de pago.

cliente = int(input("Ingrese numero cliente: "))
factura = float(input("Ingrese monto de factura: "))
while (factura < 0):
    print("ERROR -> INGRESE VALOR VALIDO DE FACTURA")
    factura = float(input("Ingrese monto de factura: "))

beneficio10 = factura
if ((factura * 0.02)>200):
    beneficio10 = beneficio10 - (factura * 0.02)
else:
    if(factura<=200):
        beneficio10 = 0
    else:
        beneficio10 = beneficio10 - 200
        
vencido = factura
if((factura*.1)>350):
    vencido = vencido + (factura * .1)
else:
    vencido = vencido + 350

print(f"FACTURA: ${factura}")
print(f"-----> PAGO DEL DIA 1 - 10: ${beneficio10}")
print(f"-----> PAGO DEL DIA 11 - 20: ${factura}")
print(f"-----> PAGO FUERA DE TERMINO: ${vencido}")
