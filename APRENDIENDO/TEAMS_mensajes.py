import pyautogui
import pyperclip
from time import sleep
import textwrap

sleep(10)
contador = 9
mensajeA = ''

for _ in range(contador):
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','c') #guardar usuario
    usuario = pyperclip.paste()

    mensaje1 = textwrap.dedent('''\
    Hola, ¿cómo estás?

    El presente mensaje es para informarte por escrito de tus credenciales tanto en Iceberg Productivo como en Pruebas:

    Para Iceberg Productivo:
    USUARIO: {}     CONTRASEÑA: Prdiceberg2023*  
    DATABASE: unitec     
    :::::::::::: AMBIENTE DE PRODUCCIÓN

    Y para tu Iceberg de Pruebas:
    USUARIO: {}     CONTRASEÑA: iceberg2023*  
    DATABASE: unitec     
    :::::::::::: AMBIENTE DE PRUEBAS
    '''.format(usuario, usuario))

    mensaje2 = textwrap.dedent('''\
    Hola, ¿cómo estás?

    Quiero confirmarte por escrito tus credenciales tanto en Iceberg Productivo como en Pruebas. Aunque ya te había notificado previamente las credenciales para el entorno Productivo, ahora deseo consolidar ambas en un solo mensaje para mayor claridad y referencia futura.

    USUARIO: {}    CONTRASEÑA: Prdiceberg2023*  
    DATABASE: unitec     
    :::::::::::: AMBIENTE DE PRODUCCIÓN

    Y para tu Iceberg de Pruebas:
    USUARIO: {}    CONTRASEÑA: iceberg2023*  
    DATABASE: unitec     
    :::::::::::: AMBIENTE DE PRUEBAS
    '''.format(usuario, usuario))

    # Resto del código...

    pyautogui.press('left',3)
    pyautogui.hotkey('ctrl','c') #comparar x
    contenido_portapapeles = pyperclip.paste().strip()
    sleep(1)
    if contenido_portapapeles == 'X':
        mensajeA = mensaje2
    else: mensajeA = mensaje1
    pyautogui.hotkey('ctrl','right')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','tab')
    sleep(1.5)
    pyautogui.click(514,24)
    pyautogui.hotkey('ctrl','v')
    sleep(2)
    pyautogui.press('down')
    pyautogui.press('enter')
    sleep(1.5)
    #contenido_actual = pyperclip.paste() #modificar papelera
    pyperclip.copy(mensajeA)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.hotkey('alt','tab')
    pyautogui.press('right')