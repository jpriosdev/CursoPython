## Tuplas
# Las tuplas son constantes, solo almacenan el valor original y no permite cambios

my_tuple = ()
my_new_tuple = tuple()

my_new_tuple = (30, 60, 60, 52, 21, 35)
my_tuple =(35, 1.80, "Juan", "Rios", "Juan", "Juan")


## Operaciones con tuplas
print("resultado de count",  my_tuple.count("Juan"))
print("Resultado de len", len(my_tuple))
print("Resultado de index Juan", my_tuple.index("Juan"))

print(my_tuple)
print(my_tuple[1]) # leer con indice en una tupla
print((my_tuple + my_new_tuple)) # concatenar las tuplas
del my_tuple # elimina por completo la tupla desaparece