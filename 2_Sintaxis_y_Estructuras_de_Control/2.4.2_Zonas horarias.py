from datetime import datetime, timedelta
from pytz import timezone
import pytz

#print (pytz.all_timezones)
print (datetime.now(pytz.timezone("Asia/Tokyo")))
print (datetime.now(pytz.timezone("Europe/Madrid")))
print (datetime.now(pytz.timezone("Zulu")))
print (datetime.now(pytz.timezone("UTC")))
print (datetime.now(pytz.timezone("Pacific/Tahiti")))