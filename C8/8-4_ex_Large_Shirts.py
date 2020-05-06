#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads
# I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = 'L'):
    """Accepts size and print it"""
    print ("\nYour shirt size is " + size + " \nI love Python.")


make_shirt("L")
make_shirt("M")
make_shirt("S" + ", love learning")

