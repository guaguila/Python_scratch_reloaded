#This is for C9 section 'IMPORTING CLASSES' in order to import classes
"""A class that can be used to represent a car."""
#You should write a docstring for each module you create.
class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name (self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer (self):
        """Print a statement showing the car's mileage."""
        print ("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer (self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >=  self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("You can't roll back an odometer!")

    def increment_odometer (self, miles):
        """Add the given amount to the odometer reading."""
        # Incrementing an Attribute’s Value Through a Method
        self.odometer_reading += miles

