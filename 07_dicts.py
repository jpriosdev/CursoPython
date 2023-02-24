### Dictionaries###

my_dict = dict()
my_other_dict ={}

my_other_dict = {"Nombre":"juan", "Apellido":"juan", "edad":40, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"juan",
    "Apellido":"juan",
    "edad":40,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.77
    }
my_dict["Nombre"] ="Juan Pablo"
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))
print(type(my_dict))
print(type(my_other_dict))
print(my_dict["Lenguajes"])

my_dict["Para borrar"] = "elemnto temporal"
print(my_dict)

del my_dict["Para borrar"]
print(my_dict)

print("Nombre" in my_dict)
print("juan2" in my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print("###############")
my_new_dict = dict.fromkeys(my_dict,"vacio") #Crea un diccionario igual al de referencia pero con vacio
print(my_new_dict)
print(list(my_dict))
print(list(my_dict.values()))
print(tuple(my_dict))
print(tuple(my_dict.values()))
print(set(my_dict))
print(set(my_dict.values()))


