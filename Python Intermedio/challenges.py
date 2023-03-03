### challenges ###

def reto1(valor_inicial, valor_final):
	#Defino variables de trabajo para asignación de valores
	valor_fizz = "fizz"
	mult_fizz = 3
	valor_buzz = "buzz"
	mult_buzz = 5

	my_list = [valor_inicial + i for i in range(valor_final)]

	for i in range(valor_final):
		if my_list[i]%mult_fizz == 0 and my_list[i]%mult_buzz ==0:
			my_list[i]="fizzbuzz"
		elif my_list[i]%mult_fizz == 0:
			my_list[i] ="fizz"
		elif my_list[i] % mult_buzz == 0:
			my_list[i] = "buzz"
	return my_list


print(reto1(1,100))
