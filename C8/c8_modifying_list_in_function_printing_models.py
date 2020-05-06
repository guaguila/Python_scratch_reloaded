#Consider a company that creates 3D printed models of designs that users submit.
# Designs that need to be printed are stored in a list, and after being printed they’re moved to a separate list.
# The following code does this without using functions:

#Modifying a List in a Function
#When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are PERMANENT, allowing you to work efficiently even when you’re dealing with large amounts of data.


# Start with some designs that need to be printed.
#This is a new line requested from Exercise 8-15 to learn functions
import c8_ex_8_15_printing_functions



#These functions (print_models, show_completed_models) were placed in according to Exercise 8-15
#I am marking them as comments in order to fulfill the exercise

#def print_models (unprinted_designs, completed_models):
    # Simulate printing each design, until none are left
    # Mode each design to completed models after printing
#    while unprinted_designs:
#        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
#        print("Printing model: " + current_design)
#        completed_models.append(current_design)


#def show_completed_models (completed_models):
#    """Show all the modesl that were printed"""
#    print ("\nThe following models have been printed:")
#    for completed_model in completed_models:
#        print (completed_model) #changes made to the list inside the function’s body are PERMANENT


unprinted_designs = ['iphone_case', 'robot pendant', 'sermon_app']
completed_models = []


#print_models (unprinted_designs[:], completed_models)
#print_models (unprinted_designs, completed_models)
c8_ex_8_15_printing_functions.show_completed_models (completed_models)
    # calling the module_name.function_name()


print(unprinted_designs)

#Preventing a Function from Modifying a List
#Sometimes you’ll want to prevent a function from modifying a list. For example, say that you start with a list of unprinted designs and write a function to move them to a list of completed models, as in the previous example. You may decide that even though you’ve printed all the designs, you want to keep the original list of unprinted designs for your records. But because you moved all the design names out of unprinted_designs, the list is now empty, and the empty list is the only version you have; the original is gone. In this case, you can address this issue by passing the function a copy of the list, not the original. Any changes the function makes to the list will affect only the copy, leaving the original list intact.




#We set up a list of unprinted designs and an empty list that will hold the completed models. Then, because we’ve already defined our two functions, all we have to do is call them and pass them the right arguments. We call print_models() and pass it the two lists it needs; as expected, print_models() simulates printing the designs. Then we call show_completed_models() and pass it the list of completed models so it can report the models that have been printed. The descriptive function names allow others to read this code and understand it, even without comments.