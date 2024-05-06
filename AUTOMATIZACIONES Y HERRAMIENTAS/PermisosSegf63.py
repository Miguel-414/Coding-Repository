# Lleve su puntero a la esquina superior derecha en caso de emergencia
# Este codigo asigna permisos a determinada persona sobre la SEGF63,
# se empieza por un excel toma el codigo del programa, se muda a la ventana mas cercana y en 
# determinado lugar especificado coloca el codigo y asigna el permiso
import pyautogui as py
import time
time.sleep(8)
contador = 154
init = time.time()
for i in range(contador):
    py.press('down')
    py.hotkey('ctrl','c')
    py.hotkey('alt','tab')
    py.doubleClick(-758,351)
    py.hotkey('ctrl','v')
    py.press('enter')
    time.sleep(1.6)
    py.click(-819,414)
    py.click(-976,375)
    time.sleep(1.6)
    py.hotkey('alt','tab')

end = time.time()    
print(end - init)