import pyautogui




def automacion():
    try:


        while True:
            # Presiona Ctrl + V
            pyautogui.hotkey('ctrl', 'v')

            # Presiona la flecha hacia abajo
            pyautogui.press('down')

            # Pausa para evitar una ejecución demasiado rápida y permitir que puedas detener el programa
            
    except KeyboardInterrupt:
        
        print("Automatización detenida manualmente.")

if __name__ == "__main__":
    automacion()

