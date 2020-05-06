#This module was created to aboard exercise 9-11
#It contains the classe user, admin and privileges
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



class Privileges:
    """Describe the access levels or privileges per users."""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Describe the administrator set of privileges"""
        print("These are the privileges:")
        for i in self.privileges:
            print("\t" + "- " + str(i).title())