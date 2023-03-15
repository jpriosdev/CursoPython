### challenges ###

from typing import Any
def fizz_buzz(valor_inicial, valor_cantidad_valores, mult_fizz, mult_buzz):
	''''* reto0
	 * Escribe un programa que muestre por consola (con un print) los
	 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
	 * cada impresión), sustituyendo los siguientes:
	 * - Múltiplos de 3 por la palabra "fizz".
	 * - Múltiplos de 5 por la palabra "buzz".
	 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
	'''

	# Defino variables de trabajo para asignación de valores
	valor_fizz = "fizz"
	mult_fizz = 3
	valor_buzz = "buzz"
	mult_buzz = 5

	# creación de lista con valores entre los valores indicados en los parámetros
	my_list = [valor_inicial + i for i in range(valor_cantidad_valores)]

	# recorremos la lista y validamos si es valor es fizz o buzz
	# para ello hacemos un for y validamos el módulo del valor indicado que si es = a cero es porque no tiene residuo
	# al final retornamos la lista completa con los valores modificados
	for i in range(valor_cantidad_valores):
		if my_list[i] % mult_fizz == 0 and my_list[i] % mult_buzz == 0:
			my_list[i] = "fizzbuzz"
		elif my_list[i] % mult_fizz == 0:
			my_list[i] = "fizz"
		elif my_list[i] % mult_buzz == 0:
			my_list[i] = "buzz"
	return my_list
def anagram(palabra_1, palabra_2):
	'''  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean)
	 según sean o no anagramas.
	 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
	 * NO hace falta comprobar que ambas palabras existan.
	 * Dos palabras exactamente iguales no son anagrama.'''

	# Ponemos toas las letras en minúsculas para poder comparar las letras y homogenizar el formato
	palabra_1 = palabra_1.lower()
	palabra_2 = palabra_2.lower()

	# mostramos las palabras luego de la normalización
	print(palabra_1)
	print(palabra_2)
	# mostramos las letras de las palabras organizadas en orden alfabético
	print(sorted(palabra_1))
	print(sorted(palabra_2))
	# Validamos si son iguales o nó
	if sorted(palabra_1) == sorted(palabra_2):
		return True
	else:
		return False
def fibonacci(number_cuantity: int):
	'''/*
	 * Escribe un programa que imprima los X primeros números de la sucesión
	 * de Fibonacci empezando en 0.
	 * - La serie Fibonacci se compone por una sucesión de números en
	 *   la que el siguiente siempre es la suma de los dos anteriores.
	 *   0, 1, 1, 2, 3, 5, 8, 13...
	 */'''

	previous_value = 0
	current_value = 1
	result = list()

	for i in range(0, number_cuantity):
		print(previous_value)
		fib = previous_value + current_value
		previous_value = current_value
		current_value = fib
		result = fib
	return result
def prime(initial, final_value_int: int):
	'''/*
	 * Escribe un programa que se encargue de comprobar si un número es o no primo.
	 * Hecho esto, imprime los números primos entre 1 y 100.
    */'''

	my_list_int = list() # Crear lista para almacenar los numeros base del calculo
	my_primes_list_int = list() #Lista para almacenar los primos
	is_divisible_bool = False #Indicador si un número es divisible

	for base_number_int in range(initial , final_value_int): #Ciclo para recorrer el rango indicado
		my_list_int.append(base_number_int) # Primer número de la lista

		for divisor_int in my_list_int: # Ciclo para tomar el número base y dividirlo con los demas de my_list_int
			if divisor_int >= 2: #el cero no es divisible por si mismo y e uno por definición no es primo
				#Se calcula el múdulo del numero base con cada número existente en la lista para ver si es divisible
				# en caso de ser divisible por algún número menor o igual a si mismo se considera divisible y no primo
				# se finaliza el ciclo con un brake y
				if (base_number_int % divisor_int == 0) and divisor_int<base_number_int:
					is_divisible_bool = True
					break # Si es divisible por cualquiera de los números previos diferentes a él no es primo
		if is_divisible_bool == False and divisor_int>1: my_primes_list_int.append(my_list_int[divisor_int-1])
		is_divisible_bool = False
	return my_primes_list_int


	'''/*
	* Crea una única función (importante que sólo sea una) que sea capaz
	* de calcular y retornar el área de un polígono.
	* - La función recibirá por parámetro sólo UN polígono a la vez.
	* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
	* - Imprime el cálculo del área de un polígono de cada tipo.
	*/ '''
def area_polygon():
	type_polygon_int = '1'
	while type_polygon_int != '4':
		print('*************************************************************************')
		type_polygon_int = input("Esta funcionalidad para  calcula el área de un poligono regular \n"
		                          " 1.Triangulo. \n 2.Cuadrado. \n 3.Rectangulo. \n 4.Salir \n"
		                          "ingrese la opición: \n")
		try:
				match type_polygon_int:
					case '1':
							base_triangle_float = float(input("Ingrese la base: \n"))
							high_triangle_float = float(input("Ingrese la altura: \n"))
							area_triangle_float = base_triangle_float * high_triangle_float/2
							print('*************************************************************************')
							print("El área del triangulo es :", area_triangle_float)

					case '2':
						side_square_float = float(input("Ingrese el lado: \n"))
						area_square = side_square_float**2
						print('*************************************************************************')
						print("El área del cuadrado es :", area_square)

					case '3':
						side1_rectangle_float = float(input("Ingrese el lado 1: \n"))
						side2_rectangle_float = float(input("Ingrese el lado2: \n"))
						area_rectangle = side1_rectangle_float * side2_rectangle_float
						print('*************************************************************************')
						print("El área del rectangulo es :", area_rectangle)

					case '4':
						print("********** Ha seleccionado salir. Gracias *******************")

					case other :
						print("!!!!!!!!!!! Has ingresado una opción inválida !!!!!!!!!!!!!")
		except Exception as ValueError:
					print("!!!!!!!!!!!!!!!!!! Se ha presentado un error !!!!!!!!!!!!!!!!!")
					print("  \t El valor ingresado no es un valor numérico ")
					print("********** Será direccionado nuevamente al menu ppal *******************")

def reto9():
	import re
	from unidecode import unidecode

	def palabra_to_dic_count(text: str) -> dict[str, int]:
		no_number_text = re.sub(r"\d+", "", text.lower())
		no_punt_text = re.sub(r"\[^\w\s]", no_number_text)

		char_counter = dict()

		for char in text:
			if char in char_counter.keys():
				char_counter[char] += 1
			else:
				char_counter = 1
		return char_counter

	def __char_counter(text: str) -> dict[str, int]:
		char_counter[char] = 1
		return char_counter
	def isHeterogram(text: str) -> bool:
		for counter in char_counter(text).values():
			if counter > 1:
				return False
		return True

	def isIsogram(text: str) -> bool:
		return True


	def isPangram(text: str) -> bool:
		return True



######################################### llamado de las funciones ###############################
# print(fizz_buzz(1, 20, 3,5))
# print(anagrama("Sica", "casi")
# print(primo(1,100))
# print(fibonacci(80)
print("hola")
area_polygon()

