
#If you dont use the str() funcion on the 'age' variable, 
#since its an integer it wouldnt be recognized as that when printed
#and since you are mixing strings(text) and numbers (integers)
#it would show an error. 
 
age = 23
message = "Happy " + str( age) + "rd Birthday!"

print (message)



#Python now knows that you want to convert the numerical value 23 to a 
#string and display the characters 2 and 3 as part of the birthday message.
# Now you get the message you were expecting, without any errors:

#Happy 23rd Birthday!


#Instead of 1.5, Python returns 1. Division of integers in Python 2 results in an integer with the remainder truncated. 
#Note that the result is not a rounded integer; the remainder is simply omitted.

#To avoid this behavior in Python 2, make sure that at least one of the numbers is a float. By doing so, the result will be a float as well

print(5 + 3)

print(10 - 2.5)


my_number = 10

print(my_number)


#import this

