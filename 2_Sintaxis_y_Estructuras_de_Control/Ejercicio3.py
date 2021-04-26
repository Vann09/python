#Crear una tabla de multiplicar
num = int(input ("Dime un numero "))
print (f"Tabla de multiplicar del {num}")

for f in range (1,11):
    multiplicacion = num * f
    print (f"{num} x {f} = {multiplicacion}")
