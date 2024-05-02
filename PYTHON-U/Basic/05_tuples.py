my_tuple = tuple()
my_other_tuple = ()
my_tuple = (23,76,89,34,43,56,75,87,32)
print(my_tuple)
print(my_tuple.index(43))
# las tuplas no se les puede modificar su contenido
# digamos queremos modificar
# my_tuple[2] = "Miguel"
# esto es imposible de modificar en una tupla
my_tuple = list(my_tuple) # convertir la tupla a una lista 
print(type(my_tuple))  