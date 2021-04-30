def Add (lista):
    while (len(lista) < 10):
        num = input ("Dime 10 números: ")
        if (num.isdigit()):
            lista.append(int(num))
        else:
            print (f"{num} no es un número")

def Calc (lista):
    par = 0
    impar = 0
    sum = 0
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

numeros = []
Add(numeros)
Calc(numeros)

