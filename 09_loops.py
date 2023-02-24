###Curso de ciclos, loops, bucles ###

#While


my_condition = 0

while my_condition <= 10:
    print(my_condition)
    my_condition += 1
    if my_condition == 8:
        print("El contador llegó a 8")
        #break
else:
    print("No se cumple la condición")

print("Finaliza la ejecución")

#For
print("Inicia el for para lista")
my_list = [15, 25, 45, 89, 78, 65, 23, 10, 25, 98]

for element in my_list:
    print(element)
else:
    print("Finaliza la lista")

print("Inicia el for para tupla")
my_tuple =(35, 1.80, "Juan", "Rios", "Juan", "Juan")

for element in my_tuple:
    print(element)
else:
    print("Finaliza la tupla")

my_other_set = {"Juan", "Rios", 1.80, 41 }

print("Inicia el for para Set")
#imprime las keys no los values

for element in my_other_set:
    print(element)
else:
    print("Finaliza el set")

print("Inicia el for para dict")
my_dict = {
    "Nombre":"juan",
    "Apellido":"juan",
    "edad":40,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.77
    }

for element in my_dict.values():
    print(element)
else:
    print("Finaliza el diccionario")
