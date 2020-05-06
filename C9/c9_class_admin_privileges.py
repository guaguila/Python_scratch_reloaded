from c9_class_user import *

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