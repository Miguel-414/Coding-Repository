import time
import pyautogui

# Esperar 5 segundos antes de iniciar
time.sleep(7)

# Definir el número de repeticiones
num_repeticiones = 2  # Cambia este valor según tus necesidades

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

    pyautogui.doubleClick(536, 244)
    pyautogui.press('delete')

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1.8)

    pyautogui.click(572, 302)
    time.sleep(2.8)

    pyautogui.press('pagedown')
    time.sleep(0.7)
    pyautogui.click(723, 307)

    pyautogui.click(576, 540, clicks=2)
    time.sleep(3)
    # Control + C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.7)
    # pyautogui.mouseUp()

    pyautogui.press('home')

    pyautogui.hotkey('alt', 'tab')

    # Control + v
    pyautogui.hotkey('ctrl', 'v')



