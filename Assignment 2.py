'''Write a python program that :
Check if the number is even or odd'''
#This is a program which shows us that the number is Even or Odd
a=int(input("Enter a number : "))
if a % 2 == 0:
    print(a,"is an Even number. ")
else :
    print(a,"is an Odd number.")
'''Task 2: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''
print("'\nSecond Task is Here"'')
sum = 0  #this is variable sum that store value of sum
for num in range(1, 51):#in this statement num is a variable which has range from 1 to 50
    sum += num   # add each number to the sum
print("\t\nThe sum of numbers from 1 to 50 is:", sum)#Here Print the sum
