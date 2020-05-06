#motorcycles.py

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducatti'
print(motorcycles)

#Appending Elements to the End of a List
#The simplest way to add a new element to a list is to append the item to the list.
motorcycles.append('BMW')
print (motorcycles)



cars = []

cars.append('volvo')
cars.append('jaguar')
cars.append('mercedes benz')


print ("\nMy favorite cars are:")
print (cars)



motorcycles.insert(0, 'TVS')
print(motorcycles)

del motorcycles[0]
print(motorcycles)


#The pop() method removes the LAST item in a list, but it lets you work 
#with that item after removing it.
print ("\nPop method")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


#Remove items using remove command
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive.")



