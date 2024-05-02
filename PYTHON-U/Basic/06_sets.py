my_set = set()
my_other_set = {"Miguel","Pachon",19}
print(my_other_set) # no es una estructura ordenada
# un set no admite repetidos my_other_set.add("Miguel ")
print("Miguel" in my_other_set)# comprueva su existencia y devuelve true
print("Miguel1" in my_other_set)
# se trabaja muy rapido con elementos que
# no necesitan estar ordenadas y que no admite repetidos
# el del borra todo un objeto
my_new_set = {"Violeta","git","Miguel"}
my_set = my_new_set.union(my_other_set) # une dos sets y no deja repetidos
print(my_set)
print(my_new_set.difference(my_other_set))