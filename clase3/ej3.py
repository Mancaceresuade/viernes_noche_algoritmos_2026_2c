importe = int(input("Ingrese precio de venta"))
if importe >= 30000:
    descuento = 5
else:
    descuento = 2
    
importeConDescuento = importe - (importe * descuento / 100)
print(importeConDescuento)