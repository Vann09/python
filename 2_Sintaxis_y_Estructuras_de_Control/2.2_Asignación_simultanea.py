#####################################################################
# Asignación Simultanea                                             #
#####################################################################
#                                                                   #
#   Sintaxis: [var1], [var2] = [var2], [var1]                       #
#                                                                   #
#   Ejemplos:                                                       #
#       a = 10                                                      #
#       b = 5                                                       #
#       a,b = b,a                                                   #
#                                                                   #
#####################################################################

#Cambio b por a. Intento 1. Forma mala
a = 5
b = 10
a = b #a vale 10 al asignar el valor de b
b = a #b vale 10 porque coge el valor asignado previamente a a
print("Intento 1. Forma mala.")
print(a)
print(b)
print("")

#Cambio b por a. Intento 2. Forma que funciona
a = 5
b = 10

temp = a #Asigno a temp el valor de a (5)
a = b
b = temp #b vale 5 porque coge el valor asignado a temp
print("Intento 2. Forma que funciona.")
print(a)
print(b)
print("")

#Cambio b por a. Intento 3. Forma de Python
a=5
b=10
a,b = b,a  #Semanticamente indica a Python que debe evaluar todas las expresiones de la parte derecha de = en primer lugar y asignar los valores resultantes de las evaluaciones a las variables de la parte izquierda del operador de asignacion (a=b, b=a)#

print("Intento 3. Forma de Python.")
print(a)
print(b)
print("")