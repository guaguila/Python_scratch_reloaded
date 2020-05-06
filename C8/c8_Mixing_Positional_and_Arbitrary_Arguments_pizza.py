#Mixing Positional and Arbitrary Arguments
#If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print ("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print ("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

