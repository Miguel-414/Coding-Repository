# Lleve su puntero a la esquina superior derecha en caso de emergencia
# Este codigo actualiza los correos sobre sinu de una manera brusca,
# el ambiente sobre el que fue diseñado es especifico 
# se debe preparar el ambiente para ejecutar este codigo y modificar los valores o
# cordenadas segun sus necesidades
# Este codigo analizo el comportamiento de sinu ante acciones rapidas tenga cuidado

import time
import pyautogui

time.sleep(12) # Tiempo de espera antes de iniciar con el codigo
num_repeticiones = 362 # Definir el número de repeticiones
# Cambia este valor según tus necesidades
init = time.time()
for _ in range(num_repeticiones):
    pyautogui.press('down')
    pyautogui.press('left',2)
    pyautogui.hotkey('ctrl','c')
    pyautogui.press('right')
    pyautogui.hotkey('alt','tab')
    pyautogui.click(1123,235) # Clik random
    pyautogui.click(589,182) # Click para codigo estudiante
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
end = time.time()
print(end - init)