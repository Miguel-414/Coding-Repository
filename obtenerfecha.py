import datetime
import pyautogui as py

cedula = '1013598997'

def obtener_fechas_del_año(año):
    fechas = []
    fecha_actual = datetime.date(año, 1, 1)
    while fecha_actual.year == año:
        fechas.append(fecha_actual.strftime("%Y-%m-%d"))
        fecha_actual += datetime.timedelta(days=1)
    return fechas

# Cambia el año aquí si lo deseas
año = 2024
fechas_del_año = obtener_fechas_del_año(año)

for fecha in fechas_del_año:
    print(fecha)
