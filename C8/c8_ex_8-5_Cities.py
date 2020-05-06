#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function
# should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.


def city(city_nm, country_nm = 'USA'):
    print("The city name is " + city_nm.title() + " is located in " + country_nm)

city('Raleigh')
city('Charlotte')
city('Escazú', 'Costa Rica')

