from typing import Any


class Person:
    def __init__(self, name, surname) -> None: #constructor de la clase
        self.full_name = f"{name} {surname}"
        self.__name = name

    def walk(self):
        print(f"{self.full_name} esta caminando")    
      
    def get_name (self):
        return self.__name
    
    def set_name (self,nombre: str):
        self.__name = nombre

my_person = Person("Miguel","Pachon")
print(my_person.full_name)  
my_person.walk( ) 
print(my_person.get_name())
my_person.set_name("Antonio")
print(my_person.get_name())
