print("Salto \nde linea")
print("\ttabulacion en la linea")
nombre, apellido, edad = "Miguel", "Pachon", 19
print("Mi nombre es {}. \nMi apellido es {}. \nMi edad es {}".format(nombre,apellido,edad))
print("Datos: Nombre : %s, Apellido : %s, Edad : %d" %(nombre,apellido,edad))
print(f"Mi Nombre es {nombre} {apellido} y tengo {edad} años") #esta es la mejor forma

#desempaquetado de caracteres
lenguaje = 'Python'
a,b,c,d,e,f = lenguaje
print(a) # imprime p
print(c) # imprime t
print(d) # imprime h

languaje_slice = lenguaje[1:3] #se comporta como un array
print(languaje_slice) # expresa las posiciciones 1 y 2 

languaje_slice = lenguaje[1:] #se comporta como un array
print(languaje_slice) # expresa a partir de la posicion 1 hasta el final

languaje_slice = lenguaje[-2] #se comporta como un array
print(languaje_slice) # expresa de manera inversa -2 es o -1 seria n

languaje_slice = lenguaje[0:6:4] #se comporta como un array
print(languaje_slice) # Traeme del 0 al 6 pero evita cada segundo caracter
#reverse python

languaje_slice = lenguaje[::-1] #se comporta como un array
print(languaje_slice) # expresa el contenido de manera inversa nohtyP

languaje = lenguaje
print(languaje.capitalize()) # pone la primera letra en mayuscula
print(languaje.upper()) # pone todo en mayuscula
print(languaje.count("t")) # cuenta las "t" dentro del texto
print(languaje.isnumeric()) # nos dice si es un numero en este caso False
print(languaje.lower()) # todas minusculas
print(languaje.upper().isupper()) #lo convierte a mayusculas y luego lo verifica
print(languaje.isupper()) #verifica que este en mayusculas
print(languaje.startswith("Py")) #verifica si comienza por los caracteres indicados
