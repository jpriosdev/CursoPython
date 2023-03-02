### Condicionales##

my_condition = False

if my_condition: # es lo mismo que la condición my_condition == True
    print("Se ejecuta la condición del if")
else:
    print("NO ejecuta la condición del if")

my_condition = 5 * 3

if my_condition == 11 and my_condition : # es lo mismo que la condición my_condition == True
    print("Se ejecuta la condición del segundo if")
else:
    print("NO ejecuta la condición del segundo if")

if my_condition >= 10 and my_condition: # es lo mismo que la condición my_condition == True
    print("Se ejecuta la condición del tercer if")
else:
    print("NO ejecuta la condición del tercer if")

a, b, c, d = 1,0,1,1

if a>b:
    print("Se ejecuta la condición del primer if")
elif b>c:
    print("Se ejecuta la segunda del segundo if")
elif c>d:
    print("Se ejecuta la condición del tercer if")
print("Finaliza la ejecución")
print("#############")

my_string = "Texto de prueba"
if not my_string:
    print("Mi primera cadena de caracteres")