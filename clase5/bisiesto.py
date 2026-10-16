# divisible por 4
# 

anio = 2024

esBisiesta = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

print(esBisiesta)