import pyautogui as py
from time import sleep as s
cedula = '1013598997'
fecha = '2023-07-12'
s(4)
py.click(731,351)
s(1)
py.press('tab')
py.press('down')
py.typewrite(cedula)
py.press('tab')
py.typewrite(fecha)
py.click(621,453)
s(1)
py.click(655,497)