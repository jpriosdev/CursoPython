# Practica de variables


my_string_var = "My string variable"
print(my_string_var)

my_int_var = 5
print(my_int_var)
print(str(my_int_var)) # str convierte una cadena en string
print(type(my_int_var)) #type muestra el tipo de Variable
my_bool_var = True
print(my_bool_var)

print(my_string_var, my_int_var, my_bool_var)
print("Ejemplo de mensaje",my_string_var, my_int_var, my_bool_var) # concatenación de variables y textos
print(len(my_string_var))  # tamaño del contenido de la variable
name, surname, alias, edad = "Juan", "Rios", "ultrademond", 41 #variables en una sola linea
print("mi nombre completo es", name, " ", surname, " mi edad es:", edad, alias)

nombre = input("Cual es tu nombre: ")
edad = input("y tu edad:")


print("tu nombre es: ", nombre, " y tu edad es: ", edad)