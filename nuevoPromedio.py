import time
import pyautogui

# Esperar 5 segundos antes de iniciar
time.sleep(15)

# Definir el número de repeticiones
num_repeticiones = 2197  # Cambia este valor según tus necesidades

for _ in range(num_repeticiones):
    pyautogui.press('down')

    # Flecha hacia la izquierda
    pyautogui.press('left')
    pyautogui.press('left')

    # Control + C
    pyautogui.hotkey('ctrl', 'c')

    # Flecha hacia la derecha
    pyautogui.press('right')

    # Alt + Tabulador
    pyautogui.hotkey('alt', 'tab')
    #time.sleep(1)
    pyautogui.press('home')
    time.sleep(1)
    pyautogui.click(523,179)
    time.sleep(3)
    pyautogui.click(523,179)

    pyautogui.doubleClick(552,180)

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('alt', 'tab') #SE DEVUELVE A POR EL PENSUM
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('right')
    pyautogui.hotkey('alt', 'tab')
    #DOBLE CLIK
    pyautogui.doubleClick(587,182)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(710, 212)
    time.sleep(3)

    pyautogui.click(745, 409)
    time.sleep(1)
    pyautogui.click(745, 409)

    pyautogui.doubleClick(577,540)
    # time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1.5)

    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)

    # Control + v
    pyautogui.hotkey('ctrl', 'v')


