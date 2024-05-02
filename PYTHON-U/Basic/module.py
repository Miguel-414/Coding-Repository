import numpy

def main (*lista):
    numero = 0
    for element in lista:
        numero += numpy.pi
        print(f"Elemento numero {numero} : {element}")      
