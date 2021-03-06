
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

    # Incrementing an Attribute’s Value Through a Method
    def increment_odometer (self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car ('audi', 'a4', '2016')
print (my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 30
my_new_car.read_odometer()

#Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(100)
my_new_car.read_odometer()

#Incrementing an Attribute’s Value Through a Method
my_used_car = Car('toyota', 'corolla', '2001')
print (my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print ("This car has a " + str(self.battery_size) + "-kwh battery.")



class ElectricCar(Car):
    """Represent aspectos of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize atttributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        #we provided the values for the arguements but need to define them again
        #it inherits the methods from the parent class, therefore we can call them

    #It was moved to Class (above) to explain inheritance
    #def describe_battery (self):
    #    """Print a statement describing the battery size"""
    #    print ("This car has a " + str(self.battery_size) + "-kwh battery.")

    def ElectricCar (self):
        """Electric cars dont have gas tanks."""
        print ("This car doesnt need a gas tank.")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

