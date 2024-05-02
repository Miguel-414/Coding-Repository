import time
import pyautogui

# Esperar 5 segundos antes de iniciar
time.sleep(7)

# Definir el número de repeticiones
num_repeticiones = 717  # Cambia este valor según tus necesidades

for _ in range(num_repeticiones):
    pyautogui.click(243,197)
    time.sleep(0.6)
    pyautogui.press("delete", presses=2)
    pyautogui.press("enter")