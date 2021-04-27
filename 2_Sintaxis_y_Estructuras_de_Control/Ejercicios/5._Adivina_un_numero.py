import random

numero = random.randint(1,25)
print ("Intenta adivinar un numero entre 1 y 25")
intento = 0

while (numero):
    num = int(input ())
    intento += 1
    if (num < numero):
        print ("Demasiado pequeño!!")
    if (num > numero):
        print ("Demasiado grande!!")
    if (num == numero):
        break

print (f"Felicidades, el número era {numero} y has usado {intento} intentos!!")
