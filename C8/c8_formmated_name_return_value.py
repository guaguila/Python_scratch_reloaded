#Returning a Simple Value
#Let’s look at a function that takes a first and last name, and returns a neatly formatted full name:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('gustavo', 'aguilar')
print(musician)


