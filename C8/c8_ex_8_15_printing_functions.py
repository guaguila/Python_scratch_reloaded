def print_models (unprinted_designs, completed_models):
# Simulate printing each design, until none are left
# Mode each design to completed models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models (completed_models):
    """Show all the modesl that were printed"""
    print ("\nThe following models have been printed:")
    for completed_model in completed_models:
        print (completed_model) #changes made to the list inside the function’s body are PERMANENT



