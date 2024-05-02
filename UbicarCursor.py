import pyautogui
import time as t

try:
    while True:
        # Obtener coordenadas actuales del cursor
        x, y = pyautogui.position()
        print(f'Coordenadas: X={x}, Y={y}')
        t.sleep(1)
except KeyboardInterrupt:
    print("\nScript detenido.")

# ! prueba comentarios
# ? halo