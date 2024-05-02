# while
# do while
# for 

prueba_while = 2
while prueba_while >= 2:
    print(f"Contador igual a {prueba_while}")
    prueba_while += 1
    if prueba_while == 5:
        print("Se finaliza la instruccion")
        break

my_list = [23,45,76,89,23,43,45,21,17,19]
my_list.sort()
for elements in my_list:
    print(f"Elemento: {elements}") 

my_dict = {
    "Nombre":"Miguel",
    "Apellido":"Pachon",
    "Edad":19,
    "Lenguajes": {"Python","Cobol","Java","C#"},
    1:1.79,
    "Calle":"Calle 76 #12-58"
}

for elemento in my_dict:
    print(f"Values : {elemento}")
    if elemento == "Lenguajes":
        print(f"{elemento} multiples")
        continue
    