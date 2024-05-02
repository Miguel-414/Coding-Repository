import pyautogui as T
import time
import pyperclip as clip

init = time.time()
abecedario_mayusculas = [chr(i) for i in range(65, 91)]
num_repeticiones = 58  # Cambia este valor según tus necesidades
nuevo_array = []
numero_guia = 1
letra_guia = 1

for letra1 in abecedario_mayusculas:
    for letra2 in abecedario_mayusculas:
        nueva_combinacion = letra1 + letra2
        nuevo_array.append(nueva_combinacion)
        
        # Romper el bucle cuando lleguemos a la letra 'D'
        if nueva_combinacion == 'DZ':
            break

resultado = abecedario_mayusculas + nuevo_array
time.sleep(5)
descanso = 0
 
for _ in range(num_repeticiones):
     texto1 = f"BUSCARV(G2;[NI_CHAAN_2.0.xls]Datos1!$A$2:${resultado[letra_guia]}$63540;{numero_guia};FALSO)"
     texto = '=SI('+ texto1 +'="";"";'+ texto1 +')'
     clip.copy(texto)
     T.hotkey('ctrl','v')
     numero_guia += 1
     letra_guia += 1
     T.press('right')
     descanso += 1
    #  if descanso == 2:
    #     time.sleep(4) 
    #     descanso = 0

finish = time.time()
enty = finish - init
print(f"Tiempo de ejecucion para {num_repeticiones} repeticiones : {enty}")