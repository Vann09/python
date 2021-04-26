#Fechas y horas
from datetime import datetime

dt1 = datetime.now().date()
dt2 = datetime.now()
print ("Fecha1: ", dt1)
print ("Fecha2: ", dt2)
print ("Año: ", dt2.year)
print ("Mes: ", dt2.month)
print ("Dia: ", dt2.day)
print ("Hora: ", dt2.hour)
print ("Minuto: ", dt2.minute)
print ("Segundo :", dt2.second)
print (f"Hora completa:  {dt2.hour}:{dt2.minute}")
print ("")

print ("Escribe tu fecha de nacimiento: ")
fecha = input()
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date() #Y 4 caracteres, y 2 caracteres
años = dt1.year - dt3.year 

print ("Fecha3: ",dt3) 
print (f"Tienes {años} años.")