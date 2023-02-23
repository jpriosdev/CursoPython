# esto es un comentario:
# Nuestro hola mundo en python
print("Hola Python")


my_string_var = "My string variable"
my_int_var = 5
my_bool_var = True

print(type("Hola Python")) # type me dice el tipo de la variable
print(str(my_int_var)) # str convierte una cadena en string
print(type(my_int_var)) #type muestra el tipo de Variable

print("Ejemplo de mensaje",my_string_var, my_int_var, my_bool_var) # concatenación de variables y textos
print(len(my_string_var))  # tamaño del contenido de la variable
name, surname, alias, edad = "Juan", "Rios", "ultrademond", 41 #variables en una sola linea
edad = input("y tu edad:") # asignación de una entrada a una variable

print(3%4) # modulo
print(11//4)#flor división aproxima a la parte entera y no considera la partde decimal
print(3**4) # exp
print("Hola " * 4*3) # multiplica el string la cantidad de veces que indique el resultado de la operación si es entero

print(my_other_list[0])   #muestra el elemento 0 de la lista
print(my_other_list[-1])  # muestra el último elemento de la lista
print(my_list.count(25)) # count cuenta las ocurrencias del criterio de busqueda ingresado

#Asignación de listas en ordenes diferentes al secuencial
name, surname, age, height  = my_other_list[1], my_other_list[0], my_other_list[2], my_other_list[3]
my_other_list.append("jprios") # Adiciona elementos a la lista al final
my_other_list.insert(1, "Azul") # Adiciona elementos en una posición deseada

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



