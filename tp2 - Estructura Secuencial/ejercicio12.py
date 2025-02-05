#TP 2
# Estructura Secuencial
# Ejercicio 12
# Escribir un programa para convertir un número binario de 4 cifras en un número decimal.
# El número binario se ingresa como un solo número
# entero de cuatro dígitos.
# Procedimiento:
# Para convertir un número binario a decimal es necesario
# multiplicar el valor de cada dígito por el número 2 elevado a un exponente.
# Este exponente se obtiene de la posición que ocupa el dígito dentro del número,
# comenzando desde la derecha con la posición 0.
# Todos estos resultados se suman para obtener el valor final.

binario = int(input("Ingrese numero binario --> "))

# El primer digito es el de mas a la derecha para mi
primerDigito = binario % 10
binario = binario // 10

segundoDigito = binario % 10
binario = binario // 10

tercerDigito = binario % 10
binario = binario // 10

cuartoDigito = binario

decimal = (cuartoDigito * 2 ** 3)+(tercerDigito * 2 ** 2)+(segundoDigito * 2 ** 1)+(primerDigito * 2 ** 0)

print("El numero en decimal es: ",decimal)