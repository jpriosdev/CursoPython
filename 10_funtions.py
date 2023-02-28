### funciones##


## Presentación del manú principal y llamado a la funcioanlidad de la calculadora
def my_menu():
    print("Mi calculadora de dos valores va a iniciar")
    option=1
    #  Se llama la calculadora hasta que la persona indique que quiere finalizar con la opción 7
    while option != "7":
        option = input("selecciona la opción que deseas. \n 1. Suma. \n 2. Resta \n "
                       "3. Miltiplicación \n 4. Divsión \n 5. Módulo \n 6. Potenciación \n "
                       "7. Salir \n Opción: ")

        # Se valida que el usuario ingrese una opción válida
        try:
            if option in ("1", "2", "3", "4", "5", "6","7"):
                print("EL resultado para validar es: ", my_calc(option))
                input("Presione intro para continuar")
            else:
                print("INGRESE UN VALOR VÁLIDO")
        except ValueError:
            print("Solo es válido ingresar valores numéricos")

    else:
        print(".. adios calculadora")

## Función de calcular la suma de dos numeros
def my_sum(primer_valor_float, segundo_valor_float):
    resultado_float = primer_valor_float  + segundo_valor_float
    print("El resultado de la suma de ",  primer_valor_float, " y de ", segundo_valor_float, "es: ", resultado_float)
    return  resultado_float

## Función de calcular la resta de dos numeros
def my_minus(primer_valor_float, segundo_valor_float):
    resultado_float = primer_valor_float  - segundo_valor_float
    print("El resultado de la resta de ", primer_valor_float, " y de ", segundo_valor_float, "es: ", resultado_float)
    return resultado_float

## Función de calcular la multiplicación de dos numeros
def my_mult(primer_valor_float, segundo_valor_float):
    resultado_float = primer_valor_float  * segundo_valor_float
    print("El resultado de la multiplicación de ", primer_valor_float, " y de ", segundo_valor_float, "es: ", resultado_float)
    return resultado_float

## Función de calcular la división de dos numeros
def my_div(primer_valor_float, segundo_valor_float):
    resultado_float = primer_valor_float  / segundo_valor_float
    print("El resultado de la división de ", primer_valor_float, " y de ", segundo_valor_float, "es: ", resultado_float)
    return resultado_float

### Función de calcular el modulo de dos números
def my_mod(primer_valor_float, segundo_valor_float):
    resultado_float = primer_valor_float  % segundo_valor_float
    print("El resultado del modulo de ", primer_valor_float, " y de ", segundo_valor_float, "es: ", int(resultado_float))
    return resultado_float

## Función de calcular la división de dos numeros
def my_pot(primer_valor_float, segundo_valor_float):
    resultado_float = primer_valor_float ** segundo_valor_float
    print("El resultado de la potenciación de ", primer_valor_float, " elevado a la ", segundo_valor_float, "es: ",resultado_float)
    return resultado_float

## llamador de las funciones según las opciones del usuario
def my_calc(option:int):
    my_result_float =0
    if int(option) in (1, 2, 3, 4, 5, 6):
        primer_valor_float = float(input("Ingrese primer valor: "))
        segundo_valor_float = float(input("Ingrese segundo valor: "))
        primer_valor_float.__float__()
        match option:
            case '1':
                my_result_float = my_sum(primer_valor_float, segundo_valor_float)
                return  my_result_float
            case '2':
                my_result_float = my_minus(primer_valor_float, segundo_valor_float)
                return my_result_float
            case '3':
                my_result_float = my_mult(primer_valor_float, segundo_valor_float)
                return my_result_float
            case '4':
                if segundo_valor_float != 0:
                    my_result_float = my_div(primer_valor_float, segundo_valor_float)
                    return my_result_float
                else:
                    print("¡¡¡El resultado de cualquier división por cero es indeterminado(infinito)!!!!")
            case '5':
                my_result_float = my_mod(primer_valor_float, segundo_valor_float)
                return my_result_float
            case '6':
                my_result_float = my_pot(primer_valor_float, segundo_valor_float)
                return my_result_float

### Inicio del llamado de la calculadora
my_menu()

