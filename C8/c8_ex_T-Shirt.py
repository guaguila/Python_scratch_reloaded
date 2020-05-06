#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be
# printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.


def make_shirt(size):
    """Accepts size and print it"""
#    print ("Your shirt size is " + size.title() + ".")
    size = input("What is your t-shirt size?")
    print ("Your t-shirt size is " + size.title() + ".'")

make_shirt('size')

