# Obtiene las cordenadas del cursor y lo muestra en consola
# Uselo para configurar los demas codigos en determinadas pautas
import pyautogui
import time as t

try:
    while True:
        x, y = pyautogui.position() # Obtener coordenadas actuales del cursor
        print(f'Coordenadas: X={x}, Y={y}')
        t.sleep(1)
except KeyboardInterrupt:
    print("\nScript detenido.")