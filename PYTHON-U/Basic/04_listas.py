# listas
my_list = list()
my_other_list = []
print(len(my_list))
my_list = [23,45,76,89,23,43,45,21,17,19]
print(len(my_list))
my_other_list = ["Miguel","Bogota",19]
print(type(my_list))
print(type(my_other_list))
a,b,c = my_other_list
print(a)
print(my_list.count(45)) #cuenta cuantas veces se repite

# funciones con listas

my_other_list.append("Español") # inserta al final del arreglo el dato
print(my_other_list)
my_other_list.insert(2,"Antonio") # inserta el dato en el lugar especificado
print(my_other_list)
my_other_list.remove("Español") # elimina el primer dato que se encuentre especificado
# elimina un elemento que conocemos que esta dentro
print(my_other_list)
my_other_list.pop() # este elimina y devuelve el ultimo elemento
# elimina un elemento en un lugar concreto pero lo retorna 
# se puede guardar en una varible list.pop(2) return posicion 2

del my_other_list[2] # este solo elimina el elemento 2
print(my_other_list)
my_other_list.clear() 
print(my_other_list) # elimina todo dentro de la lista
print(my_list)
my_new_list = my_list
print(my_new_list)
my_new_list.reverse() # esto voltea el orden la lista
print(my_new_list)
my_new_list.sort() # ordena la lista de menor a mayor 
# si es alfabetico en orden alfabetico
print(my_new_list)