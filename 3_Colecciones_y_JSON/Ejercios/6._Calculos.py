# 1. Preguntamos 10 numeros al operador (nos aseguramos de que sean numeros y añadimos los numeros a la lista
# 2. Mostramos los numeros
# 3. Mostramos la suma total de todos, la media, cantidad de numero pares y la cantidad de numeros impares

lista = []
contador = 0
par = 0
impar = 0
sum = 0

while (contador < 10):
    contador += 1
    num = input ("Dime 10 números: ")
    if (num.isdigit()):
        lista.append(int(num))
    else:
        print (f"{num} no es un número")

for num in lista:
    sum += num
    if (num % 2 == 0):
        par += 1
    else:
        impar += 1

print (lista)
print (f"Suma total: {sum}.")
print (f"Media: {sum/len(lista)}.")
print (f"Hay {par} números pares.")
print (f"Hay {impar} números impares.")