#9-12. Multiple Modules:
# Store the User class in one module, and store the Privileges and Admin classes in a separate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from c9_class_user import *
from c9_class_admin_privileges import *


full_stack_developer = Admin ('gustavo', 'aguilar','engineer', 'cr')

full_stack_developer.greet_user()
full_stack_developer.describe_user()

#Accessing Attributes
#To access the attributes of an instance, you use dot notation.
assign_privileges = ['create','update','read','delete']
full_stack_developer.privileges.privileges = assign_privileges
full_stack_developer.privileges.show_privileges()

print ("\nAdding an item to the instance attribute list")
full_stack_developer.privileges.privileges.append('wisdom')
full_stack_developer.privileges.show_privileges()