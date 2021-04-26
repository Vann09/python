dm = float(input("Metros que has recorrido: "))
tm = float(input("Minutos que has tardado: "))

vkm = (dm/1000)/(tm/60)

if ( vkm > 75):
    print (f"Tu velocidad es de {vkm} km/h. Velocidad alta.")
elif ( 75 > vkm > 30):
    print (f"Tu velocidad es de {vkm} km/h. Velocidad media.")
else:
    print (f"Tu velocidad es de {vkm} km/h. Velocidad baja.")
