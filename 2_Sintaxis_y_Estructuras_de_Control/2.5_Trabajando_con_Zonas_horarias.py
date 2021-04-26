#####################################################################
# Trabajando con fechas - Zonas Horarias                            #
#####################################################################

from datetime import datetime, timedelta
from pytz import timezone
import pytz

#Muestra todas las zonas horarias disponibles
print (pytz.all_timezones)
print ("")

#Muestra el mismo momento en diferentes zonas horarias
print (datetime.now(pytz.timezone("Asia/Tokyo")))
print (datetime.now(pytz.timezone("Europe/Madrid")))
print (datetime.now(pytz.timezone("Zulu")))
print (datetime.now(pytz.timezone("UTC")))
print (datetime.now(pytz.timezone("Pacific/Tahiti")))