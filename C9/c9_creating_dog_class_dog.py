class Dog (): #By convention, capitalized names refer to classes in Python.
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        #The __init__() method has no explicit return statement, but Python automatically returns an instance representing this dog
        #The self parameter is required in the method definition, and it must come first before the other parameters
        """Initialize name and age attributes."""
        self.nombre = name
        self.edad = age
            #Any variable prefixed with self is available to every method in the class,
            #and we’ll also be able to access these variables through any instance created from the class.

    def sit (self):
        """Simulate a dog sitting in response to a command."""
        print (self.nombre.title() + " is now sitting.")

    def roll_over (self):
        """Simulate rolling ocer in response to a command."""
        print (self.nombre.title() + " rolled over!")

#Dog capitalized refers to the class
#my_dog lowercase refers to a single instance created from a class
my_dog = Dog ('willie', 6)
your_dog = Dog ('keyla', 12)

print ("My dog's name is " + my_dog.nombre.title() + ".")
print ("My dog is " + str(my_dog.edad) + " years old.")
my_dog.sit()

print ("Your dog's name is " + your_dog.nombre.title() + ".")
print ("Your dog is " + str(your_dog.edad) + " years old.")
your_dog.sit()


#my_dog.roll_over()
#This syntax is quite useful. When attributes and methods have been given appropriately descriptive names like name, age, sit(), and roll_over(), we can easily infer what a block of code, even one we’ve never seen before, is supposed to do.



