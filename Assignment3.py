'''Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a  Number: "))
result=factorial(n)
print('Factorial of' ,n ,"is :" ,result)

'''       Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
 Expected Output:
   '''
import math
n=float(input("Enter a  Number: "))
Square_root=math.sqrt(n)
Natural_log=math.log(Square_root)
Sine_root=math.sin(Natural_log)
print("Square root : " ,Square_root)
print("Logarithm : " ,Natural_log)
print("Sine : " ,Sine_root)