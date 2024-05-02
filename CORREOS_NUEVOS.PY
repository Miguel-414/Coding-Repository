import pyautogui
import time
num_repeticiones = 58 #numero de rotaciones
time.sleep(7)
for _ in range(num_repeticiones):
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('ctrl','v')
    #pyautogui.click(508,64) #busqueda
    time.sleep(2)
    pyautogui.hotkey('ctrl','z')
    pyautogui.hotkey('alt','tab')
    time.sleep(1)