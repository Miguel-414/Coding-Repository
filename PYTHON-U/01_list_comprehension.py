my_original_list = [35,24,67,85,93,12,26,19,17,13]
my_list = [chr(i) for i in my_original_list]
print(my_list)
print()
char = chr(64)
print(char)
expresion = 0
for i in my_list: print(i)
my_num_list = [i ** i for i in range(8)]
print(my_num_list)

prueba = set(range(0,10))
print(prueba)

def sum_num (num):
    return num ** 5

nuevo_array = list(sum_num(i) for i in range(10))
print(f"--> {nuevo_array}")

print("AQUI SON CHARS \n_init_ :")
import pyautogui as py
from time import sleep   
import pyperclip as pip
from pyautogui import press
sleep(5)
#py.hotkey('alt','64')
py.keyDown('alt')
py.press('6')
py.press('4')
#py.keyUp('alt')
for i in range(1):
    # pip.copy(f"{i} --> {chr(i)}")
    # py.hotkey('ctrl','v')
    #py.typewrite(f"{i} --> {chr(i)}")
    #py.press('enter')
    print(f"{i} --> {chr(i)}") # limite de char 55295
    