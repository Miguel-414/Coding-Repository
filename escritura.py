import pyautogui as py 
import time as t
numero = 6
texto = "=BUSCARV(CE3;'[18 enero 2024  sinu.BAS_TERCERO.xlsx]Exportar Hoja de Trabajo'!$A$2:$E$63062;" + str(numero) + ";FALSO)"

t.sleep(3)
py.typewrite(texto)