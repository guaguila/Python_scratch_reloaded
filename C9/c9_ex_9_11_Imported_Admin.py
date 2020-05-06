#9-11. Imported Admin:
# Start with your work from Exercise 9-8 (page 178). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

from c9_class_admin import *
#Importing All Classes from Module c9_class_admin


full_stack_developer = Admin ('gustavo', 'aguilar','engineer', 'cr')

full_stack_developer.greet_user()
full_stack_developer.describe_user()

assign_privileges = ['create','update','read','delete']


#Accessing Attributes
#To access the attributes of an instance, you use dot notation.
full_stack_developer.privileges.privileges = assign_privileges
full_stack_developer.privileges.show_privileges()

#Structure:
#instance.object.attribute
#I can access the attribute on the instance like this: instance.object.attribute
print ("\nThis is a test that I performed cause I had a confusion accesing the attribute and the dot notation")
full_stack_developer.privileges.privileges.append('test')
#Then to print it we can access that structure also:
for i in full_stack_developer.privileges.privileges:
    print (i)



#full_stack_developer.privileges = assign_privileges
#for i in full_stack_developer.privileges:
#    print (i)
#If we add 'assign_privileges', which is a list, like above, then is added as a regular list attribute to 'full_stack_developer'. However, if we the introduce the code as the line above using privileges.privileges then we are creating the same list attribute, BUT, as an instance from Privileges class. That is why the double dot notation. Then in order to print the method show_privilege is located inside Privileges. That is how we can access it. #Structure:
#instance.object.attribute



