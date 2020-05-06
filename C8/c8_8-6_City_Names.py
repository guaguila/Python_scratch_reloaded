#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:

#"Santiago, Chile"

#Call your function with at least three city-country pairs, and print the value that’s returned.


def city_country(city, country):
    """return a string formatted """
    address = city.title() + ", " + country.upper()
    return address

i_city = input("Enter the name of the city: ")
i_country = input ("Enter the name of the country: ")

formatted_address = city_country(i_city, i_country)
print ("Your future home is in: " + formatted_address)

#REMEMBER: When you call a function that returns a value, you need to provide a variable where the return value can be stored.
#You cannot use the function result directly. That is why you need a variable to store it.
#One thing is the the function name and the arguments it receives, another the 'return value'.




