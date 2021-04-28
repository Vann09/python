# 1. Preguntamos 10 número al operador (nos aseguramos de que son números)
#    y añadimos los números al Lista
#
# 2. Mostramos los números
#
# 3. Mostramos por pantalla la suma total de todos, la media, el cantidad de números pares 
#    y la cantidad de números impares.

#Función para insertar x items en una lista
#Parámetro array: lista donde se insertan los número
def Add (array):
    while (len(array) < 10):
        num = input ("Dime 10 números: ")
        if (num.isdigit()):
            lista.append(int(num))
        else:
            print (f"{num} no es un número")

#Función de Calculos
#Parámetro array: lista donde se realizan los calculos
def Calc (array):
    par = 0
    impar = 0
    sum = 0
    for num in numeros:
        sum += num
        if (num % 2 == 0):
            par += 1
        else:
            impar += 1
    print (lista)
    print (f"Suma total: {sum}.")
    print (f"Media: {sum/len(array)}.")
    print (f"Hay {par} números pares.")
    print (f"Hay {impar} números impares.")

numeros = [] #Array en cuestión
Add(numeros) #Meto la array que sea, en este caso [numeros]
Calc(numeros)