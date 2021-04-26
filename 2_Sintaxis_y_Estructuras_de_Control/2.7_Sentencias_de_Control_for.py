#####################################################################
# Sentencias de Control - For                                       #
#####################################################################
#                                                                   #
#   Sintaxis: for [variable] in [variable colección]                #
#             print([variable])                                     #
#                                                                   #
#             for [variable] in range([inicio], [fin], [intervalo]) #
#             print([variable])                                     #
#                                                                   #
#####################################################################

# Utilizamos FOR para recorrer colecciones.
# Cuando fruta es igual a líma se finaliza el for con break, por lo que no
# muestra el valor de lima.
citricos = ["naranja", "limón", "pomelo", "líma", "toronja", "mandarina"]
for fruta in citricos:
  print(fruta)
  if fruta == "líma": 
      break
print ("")
# Utilizamos FOR con RANGE para establecer un contador y ejecutar 
# sentencias repetidas veces.
# Ejemplo: de 0 a 99 de 10 en 10
for i in range(0, 100, 10):
    print(f"Número: {i}")