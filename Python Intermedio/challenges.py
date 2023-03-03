### challenges ###

''''* reto1
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def reto1(valor_inicial, valor_cantidad_valores, mult_fizz, mult_buzz):
	#Defino variables de trabajo para asignación de valores
	valor_fizz = "fizz"
	mult_fizz = 3
	valor_buzz = "buzz"
	mult_buzz = 5

#creación de lista con valores entre los valores indicados en los parámetros
	my_list = [valor_inicial + i for i in range(valor_cantidad_valores)]

#recorremos la lista y validamos si es valor es fizz o buzz
# para ello hacemos un for y validamos el módulo del valor indicado que si es = a cero es porque no tiene residuo
# al final retornamos la lista completa con los valores modificados
	for i in range(valor_cantidad_valores):
		if my_list[i]%mult_fizz == 0 and my_list[i]%mult_buzz ==0:
			my_list[i]="fizzbuzz"
		elif my_list[i]%mult_fizz == 0:
			my_list[i] ="fizz"
		elif my_list[i] % mult_buzz == 0:
			my_list[i] = "buzz"
	return my_list

#Imprimimos la lista para los randos de valores indicados
#print(reto1(1, 20, 3,5))

'''  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) 
 según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.'''

def reto2(palabra_1, palabra_2):
	palabra_1 = palabra_1.lower()
	palabra_2 = palabra_2.lower()
	print(palabra_1)
	print(palabra_2)
	print(sorted(palabra_1))
	print(sorted(palabra_2))
	if sorted(palabra_1) == sorted(palabra_2):
		return True
	else:
		return False

print(reto2("Sica", "casi"))
