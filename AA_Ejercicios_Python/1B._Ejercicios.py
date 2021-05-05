#### B1. Pregunta un número al operador y muestra el resultado de multiplicarlo por PI. Utiliza la constante "math.pi" y recuerda incluir "import math"
import math

number = float(input("Dime un número: "))
print (f"{number} x {math.pi} = {number * math.pi}")

#### B2. Muestra la raíz cuadrada del mismo número.

print (f"La raiz cuadrada de {number} es: ", math.sqrt(number))

### B3. Muestra el arco coseno del mismo número.
if (number > 1 or number < -1):
    print (f"El número no es correcto.")
else:
    print (f"El arco coseno de {number} es: ", math.acos(number))
