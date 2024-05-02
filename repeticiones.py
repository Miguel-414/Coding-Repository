import time
import pyautogui

# Esperar 5 segundos antes de iniciar
time.sleep(7)

# Definir el número de repeticiones
num_repeticiones = 56  # Cambia este valor según tus necesidades

for _ in range(num_repeticiones):
    # Flecha hacia abajo
    pyautogui.press('down')

    # Flecha hacia la izquierda
    pyautogui.press('left')

    # Control + C
    pyautogui.hotkey('ctrl', 'c')

    # Flecha hacia la derecha
    pyautogui.press('right')

    # Alt + Tabulador
    pyautogui.hotkey('alt', 'tab')
    #time.sleep(1)

    # Doble clic en x=843 y=230
    pyautogui.doubleClick(843, 230)
    #time.sleep(1)

    # Control + v
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1.8)

    # Un clic en x=840 y=292
    pyautogui.click(840, 292)
    time.sleep(2.4)

    # Un clic en x=822 y=642
    pyautogui.click(703, 658)

    # Tres clics en x=685 y=490
    pyautogui.click(685, 490, clicks=3)
    pyautogui.mouseDown() 

    # Control + C
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.mouseUp()

    # Scroll hacia arriba 4 veces
    pyautogui.press('home')

    # Alt + Tabulador
    pyautogui.hotkey('alt', 'tab')

    # Control + v
    pyautogui.hotkey('ctrl', 'v')
