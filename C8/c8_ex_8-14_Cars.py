#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

#car = make_car('subaru', 'outback', color='blue', tow_package=True)

#Print the dictionary that’s returned to make sure all the information was stored correctly.


def car_record (man, mod, **arb):
    """Create a car record"""
    record = {}
    record ['manufacturer'] = man
    record['model'] = mod
    for key, value in arb.items():
        record[key] = value

    #print (record.items())
    for i in record:
        print (i.upper() + ": " + record[i].title())


manufacturer = input("Enter the manufacturer: ")
model = input("Enter the model: ")
color = input("Enter the color: ")
automatic = input("Y/N: ")

design = car_record(manufacturer, model, color = color, aut = automatic)
#Attributes color and aut are sent to the function (car_record) and they are taken as the dictionary keys. The answers (captured in the input section) are the values.
#Note that those two attributes are sent to the function without specifying on the function the amount of variables that we are providing.
