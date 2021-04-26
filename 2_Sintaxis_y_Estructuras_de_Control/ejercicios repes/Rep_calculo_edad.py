from datetime import datetime 

fecha = input ("¿Fecha de nacimiento? ")
dt = datetime.now().date()
dt2 = datetime.strptime (fecha, "%d-%m-%Y").date()
e = dt.year - dt2.year

if (e >= 18):
    print (f"Tienes {e} años, eres mayor de edad.")
else:
    a = 18 - e
    print (f"Tienes {e} años, te faltan {a} para ser mayor de edad.")