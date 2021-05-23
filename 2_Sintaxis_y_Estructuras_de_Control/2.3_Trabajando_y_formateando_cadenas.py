#####################################################################
# Trabajando con Cadenas de Texto                                   #
#####################################################################

cadena = "Hola Mundo 1"
newcadena = cadena.replace("o","-")

print (cadena[2]) #Empieza contando desde 0
print (cadena[2:]) #Enseña desde la posicion 2 incluida
print (cadena[:2]) #Enseña hasta la posicion 2 no incluida
print (cadena[::-1]) # Imprime la frase al revés
print (cadena[2:6]) #Enseña desde 2 hasta 6 (6 no incluida)
print (cadena[-3]) #Enseña contando desde el final
print ("")

print (newcadena)
print (cadena.replace("o","+")) #Cambia la o por +
print (cadena.upper()) #Pone todo en mayus
print (cadena.lower()) #Pone todo en minus
print (cadena.capitalize()) #Pone en mayuscula la primera letra
print (cadena.title()) #Pone en mayuscula la primera letra de cada palabra
print (cadena.isdigit()) #Si contiene solo digitos, devuelve true o false
print (cadena.isupper()) #Si esta todo en mayusculas
print("")

print (len(cadena)) #Cuenta numero de caracteres, espacios en blanco los cuenta tambien
print ("")

#####################################################################
# Input y Formateo de Cadenas y Número                                      #
#####################################################################

edad = input("Dime tu edad:")
print ("Tu edad es " + edad + ".")
print ("Tu edad es {}.".format(edad))
print ("Tu edad es {e}.".format(e=edad))
print (f"Tu edad es {edad}.") #Forma optima
print ("")

numero = 100/3
print (numero)
print ("Tu resultado es {n:1.1f}.".format(n=numero)) #Enseña un decimal
print ("Tu resultado es {n:1.3f}.".format(n=numero)) #Enseña tres decimales
print ("{n:1.3f}".format(n=numero))
print (f"Tu resultado es {numero}.")