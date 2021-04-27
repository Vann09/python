# 1. Preguntamos 10 numeros al operador (nos aseguramos de que sean numeros y añadimos los numeros a la lista
# 2. Mostramos los numeros
# 3. Mostramos la suma total de todos, la media, cantidad de numero pares y la cantidad de numeros impares

lista = []
contador = 0

while (contador < 10):
    contador += 1
    num = int(input ("Dime 10 números: "))
    if (type(num) is int):
        lista.append(num)
    else:
        print ("No es correcto")

sum = 0
for s in lista:
    sum = s + sum

par = 0
impar = 0
for num in lista:
    if (num % 2 == 0):
        par += 1
    else:
        impar += 1

print (lista)
print (f"Suma total: {sum}.")
print (f"Media: {sum/len(lista)}.")
print (f"Hay {par} números pares.")
print (f"Hay {impar} números impares.")