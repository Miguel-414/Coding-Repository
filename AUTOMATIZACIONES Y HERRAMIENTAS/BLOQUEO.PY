# Lleve su puntero a la esquina superior derecha en caso de emergencia
import pyautogui
import keyboard
import pyperclip
import time
time.sleep(4) # controla el tiempo de pausa entre una accion u otra
init = time.time()
vprograma = "0"
vpensum = "0"
vnivel = "0"
arreglo = []

def on_key_event(e):
    print(f'Tecla presionada: {e.name}')
    
keyboard.hook(on_key_event) # Capturador de eventos del teclado

def secional():
    # Sistema de ordenes para el teclado mediante la lista de llaves de pyautogui
    # Trabaja manteniendo control del sistema de portapapeles
    global vprograma
    pyautogui.press('right', 2)
    pyautogui.press('z')
    pyautogui.hotkey('ctrl', 'z')
    pyautogui.hotkey('ctrl', 'c')
    vprograma = str(pyperclip.paste())
    pyautogui.press('left', 3)
    pyautogui.press('right')
    pyautogui.press('down')
    global vpensum
    pyautogui.press('right')
    pyautogui.press('z')
    pyautogui.hotkey('ctrl', 'z')
    pyautogui.hotkey('ctrl', 'c')
    vpensum = str(pyperclip.paste())
    pyautogui.press('left')
    pyautogui.press('down')
    global vnivel
    pyautogui.press('right')
    pyautogui.press('z')
    pyautogui.hotkey('ctrl', 'z')
    pyautogui.hotkey('ctrl', 'c')
    vnivel = pyperclip.paste()
    pyautogui.press('left')
    pyautogui.press('down', 2)
    comparar()

def comparar():
    while True:
        pyautogui.hotkey('ctrl', 'c')
        contenido_portapapeles = pyperclip.paste().strip()

        if contenido_portapapeles.isdigit():
            print(vprograma, "_" + vpensum, vnivel)
            pyautogui.press('left')
            pyautogui.write(vnivel)
            pyautogui.press('left')
            pyautogui.typewrite(vpensum)
            pyautogui.press('left')
            pyautogui.typewrite(vprograma)
            pyautogui.hotkey('ctrl', 'right')
            pyautogui.press('down')
            comparar()
        elif contenido_portapapeles == "Programa":
            secional()
        elif contenido_portapapeles == "Para": # Palabra clave para finalizar el algoritmo
            break
        else:
            pyautogui.press('down')

comparar()
end = time.time()
print(end - init) # Tiempo de ejecuciòn