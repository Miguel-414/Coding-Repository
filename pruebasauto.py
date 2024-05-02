import time
import pyautogui

# Esperar 5 segundos antes de iniciar
time.sleep(5)

# Definir el número de repeticiones
num_repeticiones = 3  # Cambia este valor según tus necesidades

for _ in range(num_repeticiones):
    # Flecha hacia abajo
    pyautogui.press('down')
    time.sleep(1)

    # Flecha hacia la izquierda
    pyautogui.press('left')
    time.sleep(1)

    # Control + C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # Flecha hacia la derecha
    pyautogui.press('right')
    time.sleep(1)

    # Alt + Tabulador
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

    # Doble clic en x=843 y=230
    pyautogui.doubleClick(843, 230)
    time.sleep(1)

    # Control + v
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # Un clic en x=840 y=292
    pyautogui.click(840, 292)
    time.sleep(1)

    # Un clic en x=822 y=642
    pyautogui.click(822, 642)
    time.sleep(1)

    # Tres clics en x=685 y=490
    pyautogui.click(685, 490, clicks=3)

    # Control + C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)