#### E1. Pregunta un número al operador y muestra el mensaje los siguientes mensajes:
numero = 100
print("Dime un número: ")

while (numero):
    number = int(input())
    if ((numero - number) >= 25):
        print (f"El número {number} es demasiado pequeño.")
    
    elif (numero > number):
        print (f"El número {number} es pequeño.")

    if ((number - numero) >= 25):
        print (f"El número {number} es demasiado grande.")

    elif (numero < number):
        print (f"El número {number} es grande.")

    if (numero == number):
        print(f"Has acertado, el número era {numero}.")
        break

#si la diferencia entre el valor y contenido de la variable ***numero*** es de 25 o más.

