## List comprehension ###
import random

my_original_list=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
my_list = list()

my_list =[ int(random.SystemRandom().random()*100) for i in range(15)]
my_5mult = [5*(i+1) for i in range(10)]


print(my_5mult)
print(my_list)
print(my_original_list)


