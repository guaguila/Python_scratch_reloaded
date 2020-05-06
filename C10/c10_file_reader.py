#Here’s a program that opens this file, reads it, and prints the contents of the file to the screen:


file_path = '/Users/guaguila/Documents/Coding/Python/Python_scratch_reloaded/C10/pi_digits.txt'

with open (file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())












#you first need to open the file to access it. The open() function needs one argument: the name of the file you want to open. Python looks for this file in the directory where the program that’s currently being executed is stored

#The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program but not close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents the close() statement from being executed, the file may never close. This may seem trivial, but improperly closed files can cause data to be lost or corrupted. And if you call close() too early in your program, you’ll find yourself trying to work with a closed file (a file you can’t access), which leads to more errors. It’s not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you. All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the time is right.



#Recall that Python’s rstrip() method removes, or strips, any whitespace characters from the right side of a string. Now the output matches the contents of the original file exactly:


