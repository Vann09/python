#Pregunto fecha de nacimiento y calculo si es no mayor de edad
from datetime import datetime

print ("¿Cual es tu fecha de nacimiento?")
dt = datetime.now().date()
fecha = input ()
dt2 = datetime.strptime(fecha, "%d-%m-%Y").date()
años = dt.year - dt2.year

if (años >= 18):
    print (f"Tienes {años} años, eres mayor de edad.")

else:
    edad = 18 - años
    print (f"Te faltan {edad} años para ser mayor de edad.")
