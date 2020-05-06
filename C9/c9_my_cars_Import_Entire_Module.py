import c9_class_car
#1

my_toyota = c9_car.Car ('toyota', 'corolla', '2001')
print (my_toyota.get_descriptive_name())

my_volvo = c9_car.ElectricCar('volvo', 'xc90', '2020')
print(my_volvo.get_descriptive_name())


#module_name.class_name syntax
    #module_name = the actual file.py
    #class_name syntax = the class itself

#At ➊ we import the entire car module. We then access the classes we need through the module_name.class_name syntax



