## Strings ###

my_string = "Mi primer string"
my_other_string = 'Mi segundo string'

print(len(my_string))
print(len(my_other_string))

print("my_string  \n   my_other_string ") # con salto de linea
print("my_string  \t   my_other_string ") # con salto de linea
print("my_string  \\t   my_other_string ") # con salto de linea omitido por la doble barra igual para tabulación

# Diferentes formas de darle formato a los textos#

name, surname, edad = "Juan", "Rios", 35
print("Mi nombre es: {}, mi apellido es {} y mi edad es {}, {}".format(name, surname, edad, "Gracias."))
print(f"Mi nombre es: {name}, mi apellido es {surname} y mi edad es {edad}")
print("Mi nombre es: %s, mi apellido es %s y mi edad es %d" %(name, surname, edad))

# desempaquetado de caracteres #
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division de textos#

language = "Python"
print("División de textos")

language_slice = language[1:3] # selecciona las letras en las posiciones 1 y 3 del arreglo
print(language_slice)

language_slice = language[1:] # selecciona las letras en desde la  1 hasta el final saca la cero
print(language_slice)

language_slice = language[:3] # selecciona las letras desde la  0 contando 3 del arreglo
print(language_slice)

language_slice = language[-2] # selecciona la segunda letra de atras hacia adelante
print(language_slice)

language_slice = language[-2:] # selecciona las últimas dos letras
print(language_slice)

language_slice = language[:-2] # Omite las ultimas dos letras
print(language_slice)

#Reverse
reversed_language = language[::-1] # imprime el texto al revés
print(reversed_language)

reversed_language = language[::-1] # imprime el texto al revés
print(reversed_language)


# Funciones
print(language.capitalize())
print(language.lower())
print(language.upper())
print(language.count("o"))
print(language.isalnum())
print(len(language))
print(language.capitalize().isupper())
print(language.startswith("Py"))
print(language.endswith("Py"))