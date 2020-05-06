#LOOPING THROUGH AN ENTIRE LIST
#When you want to do the same action with every item in a list, you can use Pythons for loop.

prophets = ['Samuel', 'Elijah', 'Nathan', 'Ezekiel', 'Jeremiah', 'Gustavo']

for prophet in prophets:
	print(prophet.title() + ", that was a great message!")
	print("I want to learn more from the Bible " + prophet.title() + ".\n")
 
print("Thank you, everyone for leaving a testimony and communicated the truth.")


pizzas= ['suprema', 'carnivora', '3 quesos']
for pizza in pizzas:
	print("\n" + pizza.title())
	
