#####################################################################
# Declaración de Variables                                          #
#####################################################################
#                                                                   #
#   Sintaxis: [nombre de la varible] = [valor inicial]              #
#                                                                   #
#   Ejemplos:                                                       #
#       numero = 20                                                 #
#       saludo = "Hola a todos !!!"                                 #
#                                                                   #
#####################################################################

#Declaro variables y asigno un valor inicial
numero = 10
Numero = 20
num = 0.5
saludo = "Hola a todos!!"

#Muestro contenido de las variables en pantalla
print (numero)
print(Numero)  #Cuidado, diferencia entre mayus y minus
print(num)
print (saludo)
print ("")
print((Numero - numero)*(numero / Numero))
print(numero / Numero)
print (numero % Numero) #Modulo o resto de la división
print ("Saludo:"+ saludo)
print ("")  #Lo hago por estetica al ejecutar, me pone un espacio

#Muestro tipo de variable en pantalla
print(type(numero))
print(type(num))
print(type(saludo))
print ("")

#Consulto el tipo de diferentes valores utilizando la funcion TYPE
print(type(3))
print(type(3.1))
print(type("3"))
print(type("pizza"))
print(type(1==1))
print(type({"name":"madrid", "number":27}))
print(type(("1","2","3")))
print(type(["1","2","3"]))
print(type({"1","2","3"}))