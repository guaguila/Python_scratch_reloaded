#Importing an Entire Module
#To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program. Let’s make a module that contains the function make_pizza(). To make this module, we’ll remove everything from the file pizza.py except the function make_pizza():

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print ("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print ("- " + topping)

