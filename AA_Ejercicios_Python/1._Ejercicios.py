# Secuencia de Ejercicio 01

### ***Realiza la secuencia de Ejercicio partiendo del siguiente código.***

cadena = "Hola mundo !!"
numero = 100
lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

#### A1. Pregunta el nombre de Operador y muestra un saludo incluyendo el contenido de la variable cadena.

nombre = input("Dime tu nombre: ")
print (print ((f"{cadena} Soy {nombre}")))

#### A2. Muestra el saludo en mayúsculas, minúsculas y con la letra de cada palabra en mayúsculas.

print ((f"{cadena} Soy {nombre}").upper())
print ((f"{cadena} Soy {nombre}").lower())
print ((f"{cadena} Soy {nombre}").title())

#### B1. Pregunta un número al operador y muestra el resultado de multiplicarlo por PI. Utiliza la constante "math.pi" y recuerda incluir "import math"
import math

number = float(input("Dime un número: "))
print (f"{number} x {math.pi} = {number * math.pi}")

#### B2. Muestra la raíz cuadrada del mismo número.

print (f"La raiz cuadrada de {number:2.2f} es: ", math.sqrt(number))

### B3. Muestra el arco coseno del mismo número.

print (f"El arco coseno de {number:2.2f} es: ", math.acos(number))

