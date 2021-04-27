# 1. Preguntamos 10 numeros al operador (nos aseguramos de que sean numeros y añadimos los numeros a la lista
# 2. Mostramos los numeros
# 3. Mostramos la suma total de todos, la media, cantidad de numero pares y la cantidad de numeros impares

lista = []
contador = 0

while (contador < 10):
    contador += 1
    num = int(input ("Dime 10 números "))
    if (type(num) is int):
        lista.append(num)
    else:
        print ("No es correcto")

print (lista)

sum = 0
for s in lista:
    sum = s + sum
print (sum)

m = sum / len(lista)
print (m)

for p in lista:
    if p % 2 == 0:
        print (num)


        

