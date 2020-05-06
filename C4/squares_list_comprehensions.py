#List Comprehensions
#The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code. 

squares = [value**2 for value in range(1,11)]
print(squares)



#EXERCISES
numbers1_20 = [numbers+1 for numbers in range(0,20)]
print(numbers1_20)


oddnumbers = [odd for odd in range(0,20,2)]
print(oddnumbers)

three_multiples = [three for three in range(0,31,+3)]
print(three_multiples)


cubes_till_10 = [cubes**3 for cubes in range(0,10)]
print(cubes_till_10)

