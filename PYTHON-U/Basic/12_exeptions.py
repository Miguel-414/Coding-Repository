
try:
    variable = int(input("Ingresa un numero : "))
except ValueError as error:
    print(f"El error {error}")

#print(variable)