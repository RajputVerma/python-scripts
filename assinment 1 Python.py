'''Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division'''
a=input("Enter First Number: ")
b=input("Enter Second Number: ")
a=float(a)
b=float(b)
Addition=a+b
Substraction=a-b
Multiplication=a*b
Division=a/b
print(Addition)
print(Substraction)
print(Multiplication)
print(Division)
'''Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.'''
a=input("Enter your First Name: ")
b=input("Enter your Last Name: ")
print("Hello,",(a+ b),"!","Welcome to the Python program.")