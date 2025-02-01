#TP 2
# Estructura Secuencial
# Ejercicio 8
# Leer una medida en metros y expresarla en: centimetros, pulgadas, pies y yardas
# 1 pie = 12 pulgadas
# 1 yarda = 3 pies
# 1 pulgada = 2,54cm
# 1 metro = 100cm

metros = int(input("Ingrese cantidad de metros: "))
centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print("Metros: ",metros)
print("Centimetros: ",centimetros)
print("Pulgadas: ",pulgadas)
print("Pies: ",pies)
print("Yardas: ",yardas)