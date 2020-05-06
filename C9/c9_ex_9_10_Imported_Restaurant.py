#9-10. Imported Restaurant:
# Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

from c9_class_restaurant import Restaurant

sushi_restaurant = Restaurant('saga', 'sushi')

sushi_restaurant.describe_restaurant()
sushi_restaurant.open_restaurant()



