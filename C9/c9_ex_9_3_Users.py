#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.

#Create several instances representing different users, and call both methods for each user.

#class Name ():
#    def __init__(self, att1, att2):
#        self.att1 = att1
#        self.att2 = att2


class User():
    def __init__(self, first_name, last_name, profession, country):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """Print a brief user description."""
        print ("\tFirst name: " + self.first_name.title()+
               "\n\tLast name: " + self.last_name.title() +
               "\n\tProfession: " + self.profession.title() +
               "\n\tCountry: " + self.country.upper())

    def greet_user(self):
        """Salute the user."""
        print ("\nWelcome " + self.first_name.title() + "!")

    def increment_login_attempts(self, logins): #9-5. Login Attempts
        """Increment login attempts"""
        self.login_attempts += logins
        print("We had " + str(self.login_attempts) + " logins today.")

    def reset_login_attempts(self): #9-5. Login Attempts
        """Reset the amount of logins"""
        self.login_attempts = 0
        print("Logins were reset it: " + str(self.login_attempts))

user1 = User ('gustavo', 'aguilar','engineer', 'cr')
user1.greet_user()
user1.describe_user()

user2 = User ('raquel', 'soto','wife', 'cr')
user2.greet_user()
user2.describe_user()

user2 = User ('elias', 'aguilar','son', 'cr')
user2.greet_user()
user2.describe_user()

#9-5. Login Attempts
user3 = User ('discipulo', 'nuevo','hola', 'us' )
user3.greet_user()
user3.describe_user()
user3.increment_login_attempts(2)
user3.increment_login_attempts(2)
user3.reset_login_attempts()

#print(user3.login_attempts)