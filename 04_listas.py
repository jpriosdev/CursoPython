# Ejercicio de listas

my_list  = list()
my_other_list = []

my_list = [15, 25, 45, 89, 78, 65, 23, 10, 25, 98]


print(len(my_list))
print(my_list)
print(my_list.sort())
my_list = [15, 25, 45, 89, 78, 65, 23, 10, 25, 98]

print(my_list)

my_other_list = ["Juan", "Rios", 35, 1.80]
print(my_other_list)

print(my_list[0])
print(my_other_list[0])   #muestra el elemento 0 de la lista
print(my_other_list[-1])  # muestra el último elemento de la lista
print(my_list.count(25)) # count cuenta las ocurrencias del criterio de busqueda ingresado

name, surname, age, height  = my_other_list
print(age)

#Asignación de listas en ordenes diferentes al secuencial
name, surname, age, height  = my_other_list[1], my_other_list[0], my_other_list[2], my_other_list[3]
print(name +  surname)
print(my_other_list)


my_other_list.append("jprios") # Adiciona elementos a la lista al final
my_other_list.insert(1, "Azul") # Adiciona elementos en una posición deseada
print(my_other_list)
print(type(my_other_list))

my_other_list.remove("Azul") # Elimina elementos con el dato deseado
print(my_other_list)

# Se usa mas el pop para ir desapilando
my_other_list.pop() # Elimina el último elemento
print(my_other_list)

my_other_list.pop(2) # Elimina el elemento de una posición específica
print(my_other_list)

del my_other_list[1] #Elimina el valor en una posición específica
print(my_other_list)

my_other_list.remove("Juan") # Busca un valor y lo elimina en su primera aparición
print(my_other_list)
my_other_list.clear()
print(my_other_list)


print(my_list + my_other_list) # concatenar listas
my_list = "Hola Python" # A ser un tipado dinámico los datos cambian dinámicamente de los datos
print(my_list)
print(type(my_list))

my_list = [15, 25, 45, 89, 78, 65, 23, 10, 25, 98]

print("Final punto actual ")

my_new_list = my_list
my_new_list2 = my_new_list.copy()
#print(my_list)
#print(my_new_list)
#print(my_new_list2)

print(my_list)
print(my_new_list)
print(my_new_list2)

my_new_list.reverse()

print(my_list)
print(my_new_list)
print(my_new_list2)
