#variables y buenas practicas al declararlas
my_string_variable = "My String"
print(my_string_variable)
my_int_variable = 7
my_bool_variable = True
print(my_string_variable,my_int_variable,my_bool_variable)
# variables en una sola linea
nombre, edad, genero, mayor_de_edad = "Miguel", 19, "Masculino", True
print(nombre)

# first_name = input('Cual es tu primer nombre: ')
# age = input('Cual es tu edad: ')

# print(first_name)
# print(age)

#forzar tipado
value_string: int = input("INGRESA TEXTO ")
print(type(value_string))
value_string = 12
print(type(value_string))
print().__bool__ # NO SE QUE HACE