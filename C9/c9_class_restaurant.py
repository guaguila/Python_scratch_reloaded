#9-10
#This class was created to address exercise 9-10

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #9-4. Number Served
        #self.increment

    def describe_restaurant(self):
        print ("\nThe restaurant " + str(self.restaurant_name.title()) +
               " is specialized in " + self.cuisine_type)

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


#Marking the lines below as comments since the intention with this exercise is use the classes and methonds on exercise 9-10 only
"""
customer1_restaurant = Restaurant ('novillo', 'steak')
customer1_restaurant.describe_restaurant()
customer1_restaurant.open_restaurant()

customer2_restaurant = Restaurant ('inka', 'peruvian')
customer2_restaurant.describe_restaurant()
customer2_restaurant.open_restaurant()


customer3_restaurant = Restaurant ('dcomedy', 'fusion')
customer3_restaurant.describe_restaurant()
customer3_restaurant.open_restaurant()

customer4_restaurant = Restaurant ('9-4', 'italian')
customer4_restaurant.describe_restaurant()
customer4_restaurant.open_restaurant()
customer4_restaurant.set_number_served(110)
customer4_restaurant.increment_number_served(500)
"""

