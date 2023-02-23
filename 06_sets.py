### Sets
# Un set no es una estructura ordenada es aleatorio no se permite acceder por indices
# Un set no admite dregistros duplicados

my_set = set()
my_other_set = {}

my_other_set = {"Juan", "Rios", 1.80, 41 }
print(my_other_set)

my_other_set.add("Ultra")
print(my_other_set)

my_other_set.remove("Ultra")
print("Juan" in my_other_set)
print("Juan1" in my_other_set)

my_other_set.update({"juan"})
print(my_other_set)
my_list = list(my_other_set)
print(my_list)
print(type(my_list))