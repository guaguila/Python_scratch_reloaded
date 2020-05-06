#9-6. See instructions above

#Exercises 9-1 and 9-4 taken to work on 9-6
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #9-4. Number Served
        #self.increment

    def describe_restaurant(self):
        print ("\nThe restaurant " + self.restaurant_name +
               " is specialized in " + self.cuisine_type + ".")

    def open_restaurant(self):
        print ("The restaurant " + self.restaurant_name.title() + " is now open.")

    def set_number_served (self, served):
        """Set the number of customers"""
        self.number_served = served
        print("\nNumber of customers served: " + str(self.number_served))
        #served is not part of the class arguments

    def increment_number_served(self, visits):
        """Increment the number of visits"""
        self.number_served += visits
        print ("We are getting " + str(self.number_served) + " today!")
        print("We have " + str(visits) + " people new!")
        #visit is not part of the class arguments

#print (customer1_restaurant)
#print (customer1_restaurant.restaurant_name)
#print (customer1_restaurant.cuisine_type)


restaurant_1 = Restaurant ('novillo', 'steak')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant ('inka', 'peruvian')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()


restaurant_3 = Restaurant ('dcomedy', 'fusion')
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()

#9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
restaurant_4 = Restaurant ('9-4', 'italian')
restaurant_4.describe_restaurant()
restaurant_4.open_restaurant()
restaurant_4.set_number_served(110)
restaurant_4.increment_number_served(500)

#9-6
# Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method
class IceCreamStand (Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class
        :param restaurant_name:
        :param cuisine_type:
        """
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'pistachio', 'blueberries','naranja holandesa']

    def display_flavors(self):
        """Print a statement displaying flavors."""
        print("These are the ice cream flavors they have:")
        for i in self.flavors:
            print ("\t" + i)

restaurant_5 = IceCreamStand ('Corzo', 'ice cream')
restaurant_5.describe_restaurant()
restaurant_5.display_flavors()

