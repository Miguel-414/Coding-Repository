# Lleve su puntero a la esquina superior derecha en caso de emergencia
# Este script modifica la contraseña de determinados usuarios sobre el aplicativo ICEBERG
# Tenga cuidado al usar el script asegurese de entenderlo antes de usarlo
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
