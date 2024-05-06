# Lleve su puntero a la esquina superior derecha en caso de emergencia
# Este codigo toma las cedulas de un excel y las inserta en la matf88 en busca
# de la fecha de su ingreso, para ejecutar este codigo acomode el ambiente y lea a detalle
# el funcionamiento del codigo, tenga cuidado y realize pruebas antes de ejecutar de manera definitiva
import time
import pyautogui

time.sleep(15) # Esperar 5 segundos antes de iniciar
num_repeticiones = 2197  # Definir el número de repeticiones
init = time.time()

for _ in range(num_repeticiones):
    pyautogui.press('down') 
    pyautogui.press('left') # Flecha hacia la izquierda
    pyautogui.press('left')
    pyautogui.hotkey('ctrl', 'c') # Control + C
    pyautogui.press('right') # Flecha hacia la derecha
    pyautogui.hotkey('alt', 'tab') # Alt + Tabulador
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
    pyautogui.doubleClick(587,182) #DOBLE CLIK
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(710, 212)
    time.sleep(3)
    pyautogui.click(745, 409)
    time.sleep(1)
    pyautogui.click(745, 409)
    pyautogui.doubleClick(577,540)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1.5)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)    
    pyautogui.hotkey('ctrl', 'v') # Control + v
end = time.time()
print(end - init)