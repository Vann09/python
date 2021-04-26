import time

print ("Tiempo: ", time.time())
print (time.localtime(time.time()))
print ("Año: ", time.localtime(time.time()).tm_year)
print ("Minutos: ", time.localtime(time.time()).tm_min)
print ("Milisegundos: ", int((time.localtime(time.time()).tm_sec)*100.0))
print (time.asctime(time.localtime(time.time())))