# dates
import datetime

now = datetime.datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.isoweekday(), " Dia de la semana")
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.microsecond)


fecha_nac = datetime.datetime(1981,10,13)

print("************************************")
print(now)
print_date(now)
new_date = datetime.datetime(now.year +1, now.month, now.day)
print(new_date)
print(new_date - now)
print(now -fecha_nac)
diferencia_de_fechas= datetime.timedelta(0,200, weeks=1) #La función timedelta me permite operar  con rangos de fechas
print(now + diferencia_de_fechas)