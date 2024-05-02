my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre":"Miguel","Apellido":"Pachon","Edad":19,1:"Python"}

my_dict = {
    "Nombre":"Miguel",
    "Apellido":"Pachon",
    "Edad":19,
    "Lenguajes": {"Python","Cobol","Java","C#"},
    1:1.79,
    "Calle":"Calle 76 #12-58"
}

print(len(my_other_dict))
print(len(my_dict))
print("Antonio" in my_dict) # da false
my_dict["Nombre"] = "Antonio"
print("Antonio" in my_dict) # da false
#no se busca por contenido si no por indice 
print("Nombre" in my_dict) # da true
print(my_dict["Nombre"])
print(my_dict)
del my_dict["Calle"]
print(my_dict)
print("Object")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_new_dict = dict.fromkeys(("Nombre",1,"Calle"))
# nos crea un diccionario con llaves sin valor
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
# esto realiza una copia de llaves vacias de otro diccionario
# reaprovechamiento de llaves 
my_new_dict["Nombre"] = "Miguel"
print(my_new_dict)
print(dict.fromkeys(list(my_new_dict.values())))