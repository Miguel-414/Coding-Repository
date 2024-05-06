# Lleve su puntero a la esquina superior derecha en caso de emergencia
# Este codigo escribe de manera inmediata una gran cantidad de buscarv uno tras otro, 
# trayendo la columna siguiente a buscar,
# Nota importante recuerde que en exel ya existe una formula que trae todas las columnas buscadas
# puede especificar que columnas desea traer con un dato y el orden, entre otros
import pyautogui as T
import time
import pyperclip as clip

init = time.time()
time.sleep(5)
abecedario_mayusculas = [chr(i) for i in range(65, 91)]
num_repeticiones = 58  # Cambia este valor según tus necesidades
nuevo_array = []
numero_guia = 1 # El numero de Columna desde el que comenzara a traer la información
letra_guia = 1 # Esto indica con que letra del abecedario comenzara, 1 = A, 2 = b, etc

for letra1 in abecedario_mayusculas:
    for letra2 in abecedario_mayusculas:
        nueva_combinacion = letra1 + letra2
        nuevo_array.append(nueva_combinacion)
        if nueva_combinacion == 'DZ': # Romper el bucle cuando lleguemos a la letra 'D'
            break

resultado = abecedario_mayusculas + nuevo_array
 
for _ in range(num_repeticiones):
     texto1 = f"BUSCARV(G2;[NI_CHAAN_2.0.xls]Datos1!$A$2:${resultado[letra_guia]}$63540;{numero_guia};FALSO)"
     texto = '=SI('+ texto1 +'="";"";'+ texto1 +')'
     clip.copy(texto)
     T.hotkey('ctrl','v')
     numero_guia += 1
     letra_guia += 1
     T.press('right')
    
finish = time.time()
enty = finish - init
print(f"Tiempo de ejecucion para {num_repeticiones} repeticiones : {enty}")