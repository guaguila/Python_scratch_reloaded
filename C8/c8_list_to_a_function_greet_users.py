def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['gustavo', 'raquel', 'elias']
greet_users(usernames)



#Say we have a list of users and want to print a greeting to each. The following example sends a list of names to a function called greet_users(), which greets each person in the list individually:
