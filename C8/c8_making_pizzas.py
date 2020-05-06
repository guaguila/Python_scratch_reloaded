#Importing Specific Functions
#Using as to Give a Function an Alias
#from c8_importing_modules_pizza import make_pizza as mp
#mp ((16, 'pepperoni'))
#mp ((12, 'mushrooms', 'green peppers', 'extra cheese'))


#Importing an Entire Module
#import c8_importing_modules_pizza
#c8_importing_modules_pizza.make_pizza (16, 'pepperoni')
#c8_importing_modules_pizza.make_pizza (12, 'mushrooms', 'green peppers', 'extra cheese')


#Using as to Give a Module an Alias
#import c8_importing_modules_pizza as p
#p.make_pizza (16, 'pepperoni')
#p.make_pizza (12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing All Functions in a Module
from c8_importing_modules_pizza import *
make_pizza (16, 'pepperoni')
make_pizza (12, 'mushrooms', 'green peppers', 'extra cheese')


#When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program. You don’t actually see code being copied between files because Python copies the code behind the scenes as the program runs. All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py.

#To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot

#This first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program. If you use this kind of import statement to import an entire module named module_name.py, each function in the module is available through the following syntax:

#module_name.function_name()


#Importing Specific Functions
#You can also import a specific function from a module. Here’s the general syntax for this approach:

#from module_name import function_name

#You can import as many functions as you want from a module by separating each function’s name with a comma:

#from module_name import function_0, function_1, function_2





from c8_importing_modules_pizza import make_pizza

