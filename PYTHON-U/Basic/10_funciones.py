# funciones
def valores_default(nombre,apellido, edad = 19):
    print(f"Me llamo {nombre} {apellido} y tengo {edad}")

# valores_default(input(),input())

def  uso_return(num1,num2):
    return num1 + num2

# print(uso_return(int(input()),int(input())))

def escribir(*text: str): # puedes pasar todos los parametros que se quieran
    for texto in text:
        print(f"Mi texto : {texto}")

escribir("hola","Miguel",1076220050,"algebra","Pitagoras")        