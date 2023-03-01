## Classes ##

class MyEmptyPerson:
    pass  # Para crear clases vacias sin nada


print(MyEmptyPerson())

class Person:  #Creanmos la clase Person
    def __init__(self, name, surname, alias ="El cuate"): # inicializamos el método constructor del objeto persona, con dos parámetros
        self.name = name              # Creamos propiedad name dentro de persona
        self.surname = surname        # Creamos propiedad surname dentro de persona
        self.alias = alias
        self.__fullname = (f" {name}  {surname}") # creamos una porpiedad privada la cual no se puede modificar ni acceder directamente
        print("+++++++++++", self.__fullname)
    def walk (self):
        print(f" {self.name} {self.surname} {self.alias} Está caminando")
    def get_fullname(self): # se crea la clase get_fullname para poder acceder al valor de la propiedad fullname, pero no se puede modificar
        return self.__fullname # en caso de quere modificarla debería de crear un método de modificación


class Person1:  #Creamos la clase Person
    def __init__(self,name ,surname): # inicializamos el método constructor del objeto persona, con dos parámetros
        self.fullname = f"{name} {surname}"              # Creamos propiedad name dentro de persona

my_persona = Person("Juan", "Rios")

my_persona1 = Person1("Juan Pablo", "Rios Alvarez")
print(my_persona1.fullname)
print(my_persona.name, my_persona.surname)
print(f"{my_persona.name} {my_persona.surname}")
print(my_persona.get_fullname(), "**********************")
my_persona.walk()