#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.

#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #9-4. Number Served
        #self.increment

    def describe_restaurant(self):
        print ("\nThe restaurant " + self.restaurant_name +
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

#print (customer1_restaurant)
#print (customer1_restaurant.restaurant_name)
#print (customer1_restaurant.cuisine_type)


customer1_restaurant = Restaurant ('novillo', 'steak')
customer1_restaurant.describe_restaurant()
customer1_restaurant.open_restaurant()

customer2_restaurant = Restaurant ('inka', 'peruvian')
customer2_restaurant.describe_restaurant()
customer2_restaurant.open_restaurant()


customer3_restaurant = Restaurant ('dcomedy', 'fusion')
customer3_restaurant.describe_restaurant()
customer3_restaurant.open_restaurant()

#9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
customer4_restaurant = Restaurant ('9-4', 'italian')
customer4_restaurant.describe_restaurant()
customer4_restaurant.open_restaurant()
customer4_restaurant.set_number_served(110)
customer4_restaurant.increment_number_served(500)


