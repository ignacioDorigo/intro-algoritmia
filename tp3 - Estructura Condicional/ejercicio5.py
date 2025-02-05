# TP 3
# Ejercicio 5
# Una editorial determina el precio de un libro
# según la cantidad de páginas que contiene.
# El costo básico del libro es de $500, más $3,20 por página con encuadernación rústica.
# Si el número de páginas supera las 300 páginas
# la encuadernación debe ser en tela, lo que incrementa el costo en $200.
# Además, si el número de páginas sobrepasa las 600 páginas
# se hace necesario un procedimiento especial de encuadernación
# que incrementa el costo en otros $336. Desarrollar un programa
# que calcule el costo de un libro dado el número de páginas.

paginas = int(input("Ingrese cantidad de páginas: "))
basico = 500
if (paginas<=300):
    precio = basico
    print("Precio Final : $",precio)
    
elif (paginas>300 and paginas<=600):
    precio = basico + 200
    print("Precio Final : $",precio)
    
elif(paginas>600):
    precio = basico + 200 + 336
    print("Precio Final : $",precio)