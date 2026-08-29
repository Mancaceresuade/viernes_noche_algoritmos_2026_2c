# tomar datos del teclado
edadIngresada = input("ingrese su edad")
# procesar
edad = int(edadIngresada)
if int(edadIngresada) > 17:
    aux = "Es mayor de edad"
else:
    aux = "Es menor de edad"    
# imprimir resultado
print(aux)