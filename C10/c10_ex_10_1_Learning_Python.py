filename = 'learning_python.txt'

# Write a program that reads the file and prints what you wrote three times.
with open (filename) as file_object:
    lines = file_object.readlines()
    #The method readlines() reads until EOF using readline() and returns a list containing the lines.
print ("---Print the file 3 times---")
for i in range(3):
    print(lines)

# Print the contents once by reading in the entire file
with open (filename) as file_object:
    contents = file_object.read()
    #Use read() if you need to extract a string that contains all characters in the file
print ("---Print once reading the entire file---")
print (contents)

#once by looping over the file object
with open (filename) as file_object:
    print("---Print once reading the entire file---")
    for line in file_object:
        print (line.rstrip())

#once by storing the lines in a list and then working with them outside the with block.
with open (filename) as file_object:
    list = file_object.readlines()
print ("---Print storing on a list---")
for line in list:
    print(line.rstrip())

#print(pi_string)
#print(len(pi_string))



#10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far.
# Start each line with the phrase In Python you can....
# Save the file as learning_python.txt in the same directory as your exercises from this chapter.
#
# Write a program that reads the file and prints what you wrote three times.
#
# Print the contents once by reading in the entire file,
#   once by looping over the file object,
#   and once by storing the lines in a list and then working with them outside the with block.