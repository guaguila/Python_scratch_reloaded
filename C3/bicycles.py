#In Python, square brackets ([]) indicate a list, and individual 
#elements in the list are separated by commas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
#format
print(bicycles[0].title())


print(bicycles[2])
#format
print(bicycles[2].upper())

#last element in the list
print(bicycles[-1].upper())


message = "My first bycicle was a " + bicycles[0].title()
print((message) + " and the 2nd was a " + bicycles[1].title())




