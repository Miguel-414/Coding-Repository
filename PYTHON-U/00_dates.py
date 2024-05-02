import datetime
fecha = datetime.datetime.now()
meses = {
    1 : "Enero",
    2 : "Febrero",
    3 : "Marzo",
    4 : "Abril",
    5 : "Mayo",
    6 : "Junio",
    7 : "Julio",
    8 : "Agosto",
    9 : "Septiembre",
    10 : "Octubre",
    11 : "Noviembre",
    12 : "Diciembre"
}
print(fecha.minute)
print(fecha.timestamp()) # segundos transcurridos desde 1970
print(f"Son las {fecha.hour}:{fecha.minute} con {fecha.second} segundos \
       \nDel {fecha.day} de {meses[fecha.month]} del {fecha.year}")
from datetime import time
time = time()
print(time.hour)
print(time.min)
print(time.second)

delta = datetime.timedelta(200, 100, 100, weeks = 10)
end_delta = datetime.timedelta(200, 100, 100, weeks = 13)

print(end_delta - delta )

now_date = datetime.datetime(year=fecha.year, month=fecha.month,day=fecha.day,hour=fecha.hour)
end_date = datetime.datetime(year=2024,month=5,day=6, hour=7)

print(end_date - now_date) # 2500 lineas un objeto