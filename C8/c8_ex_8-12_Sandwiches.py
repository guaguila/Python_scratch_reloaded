#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.


def create_sandwich(cust, *ingre):
    #print(cust)
    for key in ingre:
        print(key)


ingredients_list = []
customer = input("Enter the customer name:")
while True:
    print ("-Enter 'q' at any time to quit-")
    ingredients = input("Enter the ingredients: ")
    if ingredients == 'q':
        break
    else:
        ingredients_list.append(ingredients)

order = create_sandwich(customer, ingredients_list)

#print (ingredients)
#print (ingredients_list)
