favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

for name in favorite_languages.keys():
    print(name.title())

#Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote ...
#You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.

