from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['gustavo'] = 'python'

for name, language in favorite_languages.items():
    print (name.title() + " 's favorite language list is " + language.title() + ".")
#name and language are just indexes to access the dictionary. The below code will do the same than the above:
#for i, l in favorite_languages.items():
#    print (i.title() + " 's favorite language list is " + l.title() + ".")


#Dictionaries have:
    #keys
    #values
    #items
print("\nKeys:")
for i in favorite_languages.keys():
    print(i)

print("\nValues:")
for i in favorite_languages.values():
    print(i)

print("\nItems:")
for i in favorite_languages.items():
    print(i)


