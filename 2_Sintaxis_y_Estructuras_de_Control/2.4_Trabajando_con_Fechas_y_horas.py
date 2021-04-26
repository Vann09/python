#####################################################################
# Trabajando con fechas                                             #
#####################################################################
#                                                                   #
#   Sintaxis: datetime.now()                                        #
#             datetime.now().date()                                 #
#             datetime.now().today()                                #
#                                                                   #
#             datetime.strptime("11-03-1998", "%d-%m-%Y").date()    #
#             print(datetime.now().strftime("%A, %d %m, %Y")        #
#                                                                   #
#####################################################################
from datetime import datetime

#Almaceno en la variable dt1 la fecha actual del sistema
dt1 = datetime.now().date()
print ("Fecha1: ", dt1)

#Almaceno en la variable dt2 la fecha y hora actual del sistema
dt2 = datetime.now()
print ("Fecha2: ", dt2)

#
print ("Año: ", dt2.year)
print ("Mes: ", dt2.month)
print ("Dia: ", dt2.day)
print ("Hora: ", dt2.hour)
print ("Minuto: ", dt2.minute)
print ("Segundo :", dt2.second)
print (f"Hora completa:  {dt2.hour:2.0f}:{dt2.minute:2.0f}:{dt2.second:2.0f}")
print ("")

#Convertimos un valor alfanúmerico en fecha utilizando STRPTIME
print ("Escribe tu fecha de nacimiento: ")
fecha = input()
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date() #Y 4 caracteres, y 2 caracteres

#Mostramos por pantalla una fecha formateada
print("Fecha3: ", dt3.strftime("%A, %d %B, %Y"))

#Calculos entre fechas
años = dt1.year - dt3.year 
print ("Fecha3: ", dt3) 
print (f"Tienes {años} años.")