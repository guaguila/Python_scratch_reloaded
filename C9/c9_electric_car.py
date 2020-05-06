from c9_class_car import Car

class Battery():
    #doesn’t inherit from any other class, hence Battery()
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size)+ " -kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery == 85:
                range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print (message)



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize atttributes of the parent class."""
        super().__init__(make, model, year)
        #self.battery_size = 70
            # #This is grayed out because of book section "Instances as Attributes"
        self.battery = Battery()
            #we provided the values for the arguements but need to define them again
            #it inherits the methods from the parent class, therefore we can call them

#    def describe_battery (self):
#        """Print a statement describing the battery size"""
#        print ("This car has a " + str(self.battery_size) + "-kwh battery.")
            #this was moved to Battery class in order to invoke it from there

    #Overriding Methods from the Parent Class
    def fill_gas_tank(self):
        """Electric cars dont have gas tanks."""
        print ("This card doesnt need a gas tank.")