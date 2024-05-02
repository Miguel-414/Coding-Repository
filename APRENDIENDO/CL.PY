import pyautogui
from time import sleep
sleep(7)
correos = 36
#cambiar expresiones a keyboard
for _ in range(correos):
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    pyautogui.click(961,220) # random
    pyautogui.click(617,160)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    sleep(2.5)
    pyautogui.click(624,184) #registro
    sleep(0.5)
    pyautogui.click(679,480) #correo
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
    pyautogui.hotkey('alt','tab')
    sleep(0.1)
    pyautogui.hotkey('ctrl','right')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    pyautogui.click(679,480) #correo
    sleep(0.1)
    pyautogui.hotkey('ctrl','v')
    sleep(2)    
    pyautogui.click(583,169)
    sleep(1.5)
    pyautogui.hotkey('alt','tab')
    pyautogui.hotkey('ctrl','left')
