#####################################################################
# Sentencias de Control - While                                     #
#####################################################################
#                                                                   #
#   Sintaxis: while ([condición]):                                  #
#                                                                   #
#   Con while podemos ejecutar un conjunto de sentencias            #
#   siempre que la condición sea verdadera.                         #
#                                                                   #
#####################################################################

valor = 0
while (valor < 5):
    valor += 1
    print (f"Valor: {valor}")
    
print ("Fin del while")

#####################################################################

citricos = ["naranja", "limón", "pomelo", "líma"]
index = 0

while (index < len(citricos)):
    print(citricos[index])
    index += 1

print("Fin del WHILE")