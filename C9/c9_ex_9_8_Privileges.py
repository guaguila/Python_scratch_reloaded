#9-8 instructions below

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
        print("\tWe had " + str(self.login_attempts) + " logins today.")

    def reset_login_attempts(self): #9-5. Login Attempts
        """Reset the amount of logins"""
        self.login_attempts = 0
        print("\tLogins were reset it: " + str(self.login_attempts))

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

#9-7
#Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

class Admin (User):
    def __init__(self, first_name, last_name, profession, country):
        """
        Initialize attributes of the parent class
        :param first_name:
        :param last_name:
        :param profession:
        :param country:
        """
        super().__init__(first_name, last_name,profession,country)
        # Initialize an empty set of privileges. 9-8
        self.privileges = Privileges()
        #'Instances as Attributes' section on C9
        #Make a Privileges instance as an attribute in the Admin class


#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    """Describe the access levels or privileges per users."""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Describe the administrator set of privileges"""
        print("These are the privileges:")
        for i in self.privileges:
            print("\t" + "- " + str(i).title())

user4 = Admin('Jesus', 'Christ', 'Savior', 'Universe')
user4.greet_user()
user4.describe_user()

user4_privileges = ['edify', 'comfort', 'teach', 'exhort']
user4.privileges.privileges = user4_privileges
user4.privileges.show_privileges()


