#Returning a DictionaryA function can return any kind of value you need it to, including more complicated data structures
# like lists and dictionaries.


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""

    first_name = (input("Enter your first name:"))
    last_name = (input("Enter your last name:"))
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    #person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('person(first)','person(last)', age=27)

print(musician)

