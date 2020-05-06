





#8-9. Magicians: Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(list):
    """prints the name of each magician in the list"""
    print("These are the magicians:")
    for key in list:
        print(key)


magicians_names = []
#for magician in magicians_names:
while True:
    print("(enter 'q' at any time to quit)")
    magician = input("Enter magician name: ")
    if magician == 'q':
        break
    else:
        magicians_names.append(magician)


magicians_list = show_magicians(magicians_names)