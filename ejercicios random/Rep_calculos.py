# 1. Preguntamos 10 numeros al operador (nos aseguramos de que sean numeros y añadimos los numeros a la lista
# 2. Mostramos los números
# 3. Mostramos la suma total de todos, la media, cantidad de numero pares y la cantidad de numeros impares

def Intro (numbers):

    while (10 > len(numbers)):
        number = (input("Dime 10 números: "))
        if number.isdigit():
            numbers.append(int(number))
        else:
            print (f"{number} no es un número.")

def Calc (numbers):
    plus = 0
    par = 0
    impar = 0
    for number in numbers:
        plus += number
        if (number % 2 == 0):
            par += 1
        else:
            impar += 1
    print (f"Los números elegidos son {numbers}.")
    print (f"Suma: {plus}")
    print (f"Media: {plus/len(numbers)}")
    print (f"Hay {par} números pares.")
    print (f"Hay {impar} números impares.")
    
numbers = []
Intro (numbers)
Calc(numbers)


