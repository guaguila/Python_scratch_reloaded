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