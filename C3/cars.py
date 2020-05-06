#ORGANIZING A LIST
#The sort method, shown at changes the order of the list permanently. 
#The cars are now in alphabetical order, and we can never revert to the original order:


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()

print("\n" + str(cars))


cars.sort(reverse = True)
print("\n" + str(cars))
#Again, the order of the list is permanently changed:


#Sorting a List Temporarily with the sorted() Function
print(sorted(cars))

#Notice that the list still exists in its original order at after the sorted() function has been used. The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order.



euro_cars = ['mercedes', 'volvo', 'land rover', 'jaguar']
print("\n" + str(euro_cars))

euro_cars.reverse()
print(euro_cars)
#Notice that reverse doesnt sort backward alphabetically; it simply reverses the order of the list:


print (len(cars), "items")


#TRY IT YOURSELF

places = ['Colorado', 'New Zealand', 'Swiss', 'Germany', 'Japan']
print ("\n" + str(places))
print (sorted(places))

places.reverse()
print (places)

places.reverse()
print (places)
print (places[-1])








