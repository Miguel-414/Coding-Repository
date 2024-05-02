import pyautogui
from time import sleep
contraseña = 'iceberg2023*'
contador = 45
sleep(7)
for _ in range(contador):
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    sleep(0.4)
    pyautogui.press('f7')
    pyautogui.hotkey('ctrl','v')
    sleep(0.4)
    pyautogui.press('f8')
    pyautogui.click(449,334)
    sleep(1.2)
    pyautogui.click(786,451)
    sleep(1.2)
    pyautogui.write(contraseña)
    sleep(0.2)
    pyautogui.click(327,252)
    sleep(1.2)
    pyautogui.press('enter')
    pyautogui.hotkey('alt','tab')
