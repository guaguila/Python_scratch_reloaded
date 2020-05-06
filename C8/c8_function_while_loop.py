#Using a Function with a while Loop
#You can use functions with all the Python structures you’ve learned about so far. For example, let’s use the
# get_formatted_name() function with a while loop to greet users more formally.

def get_formatted (first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#This is an infite loop
while True:
    print ("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    #formatted_name is the variable used to load the function results.
    #the function results always goes inside a variable
    #then you do what you need with that value
    formatted_name = get_formatted(f_name, l_name)
    print ("\nHello, " + formatted_name + "!")

