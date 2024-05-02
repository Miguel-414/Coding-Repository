import time
import pyautogui

# Esperar 5 segundos antes de iniciar
time.sleep(12)

# Definir el número de repeticiones
num_repeticiones = 362
  # Cambia este valor según tus necesidades

for _ in range(num_repeticiones):
    pyautogui.press('down')
    pyautogui.press('left',2)
    pyautogui.hotkey('ctrl','c')
    pyautogui.press('right')
    pyautogui.hotkey('alt','tab')
    pyautogui.click(1123,235) #clik random
    pyautogui.click(589,182) #click para codigo estudiante
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('alt','tab')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('ctrl','c')
    pyautogui.press('right')
    pyautogui.hotkey('alt','tab')
    pyautogui.click(1123,235) #clik random
    pyautogui.click(626,181) #click para pensum
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(2.7)
    pyautogui.click(633,212) #registro uno
    time.sleep(2.6)
    pyautogui.click(714,411) #materia
    pyautogui.doubleClick(616,536) #porcentaje
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('ctrl','v')
    #time.sleep(2)