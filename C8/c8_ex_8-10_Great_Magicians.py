




#8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase the
# Great to each magician’s name.
#
# Call show_magicians() to see that the list has actually been modified.

def show_magicians(list):
    """prints the name of each magician in the list"""
    print("These are the magicians:")
    for key in list:
        print(key)

def make_great (list):
    """Modifies the function"""
    great_magicians = []
    magicians = []
    while list:
        magicians = list.pop()
        name_format = magicians + ' the great'
        great_magicians.append(name_format)

        #magician = list.pop()
        #name_format = magician + ' the great'
        #great_magicians.append(name_format)

    return great_magicians


magicians_names = []
#for magician in magicians_names:
while True:
    print("(enter 'q' at any time to quit)")
    magician = input("Enter magician name: ")
    if magician == 'q':
        break
    else:
        magicians_names.append(magician)

magicians_list = make_great(magicians_names)
print (magicians_names) #Note that macigicians_names was edit in the functions when it was sent. Keep in mind function alter lists, that is why you better send a copy [:] to the functions instead of the proper list
show_magicians(magicians_list)