# from car import Car, ElectricCar
# import car
from car import *
 
my_mustang = car.Car('ford', 'mustang', 2029)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar('nissan', 'leaf', 2026)
print(my_leaf.get_descriptive_name())