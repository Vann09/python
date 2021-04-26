#Pregunto y calculo velocidad
dm = float(input ("¿Cuantos metros has recorrido? "))
tm = float(input ("¿Cuantos minutos has tardado? "))

v = (dm/1000) / (tm/60)

if (v > 75):
    print (f"Velocidad alta. Tu velocidad es de {v} km/h.")
elif (v > 30):
    print (f"Velocidad media.Tu velocidad es de {v} km/h")
else:
    print (f"Velocidad moderada.Tu velocidad es de {v} km/h")

