### Exception handling###

try: #Se controlan los errores que se puedan presentar

    mi_lista_float = list()
    entrada_str = input("ingrese los valores separados por coma")
    mi_lista_float = entrada_str.split(",")

    suma = 0
    for element in mi_lista_float:
        suma += int(mi_lista_float[int(element)-1])
    print(suma)
#Se ejecuta si se presenta algún error pero no se muestra nada de lo que este en el else
except Exception as error:#Puedo capturar de cualquier tipo y en la variable error capturo el error específico
    #Exception es el más genérico se recoienda primero los otros errores y con exception los restantes
    print("****** NO SE PUEDE SUMAR ******** ", error)


else: #Se ejecuta si no presentan errores (opcional)
    print("La ejecución ha sido exitosa")
    print(mi_lista_float)
    print(type(mi_lista_float))
    print(mi_lista_float)

finally:#Se ejecuta cuando se presentan errores despues del except (opcional)
    print("******************* la ejecución continua sin problemas pero se presentaron problemas **************")

print("Estoy fuera del manejo de excepciones")



try:

    entrada_str = input("ingrese los valores separados por coma")
    mi_lista_float = entrada_str.split(",")

    suma = 0
    for element in mi_lista_float:
        suma += int(mi_lista_float[int(element)-1])
    print(suma)
except IndexError: #capturamos todos los errores del tipo que deseamos
    print("falla un error de tipo idexerror")
except ValueError:
    print("falla un error de tipo idexerror")


