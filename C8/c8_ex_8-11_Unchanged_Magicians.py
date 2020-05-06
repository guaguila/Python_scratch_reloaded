#8-11. Unchanged Magicians: Start with your work from Exercise 8-10.
# Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.


def show_magicians(list1, list2):
    """prints the name of each magician in the list"""
    print("These are the magicians:")
    for key in list1:
        print(key)
    for key in list2:
        print(key)

def make_great (list):
    """Modifies the function"""
    great_magicians = []
    magicians = []
    while list:
        magicians = list.pop()
        name_format = magicians + ' the great'
        great_magicians.append(name_format)


    return great_magicians


magicians_names = []
#for magician in magicians_names:
while True:
    print("-Enter 'q' at any time to quit-")
    magician = input("Enter magician name: ")
    if magician == 'q':
        break
    else:
        magicians_names.append(magician)

magicians_list = make_great(magicians_names[:]) # Call the function make_great() with a copy
show_magicians(magicians_names, magicians_list)