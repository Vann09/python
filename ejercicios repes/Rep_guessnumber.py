import random

number = random.randint (0, 10)
print ("Intenta adivinar el número: ")
guess = 0

while (number == number):
    num = int(input(""))
    guess += 1
    if (num < number):
        print ("Tú número es demasiado pequeño, sigue intentandolo xP")
    if (num > number):
        print ("Tú número es demasiado grande, sigue intentandolo xP")
    if (num == number):
        print ("Felicidades, has acertado el número")
        break

print (f"Has necesitado {guess} intentos.")