'''Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''


# Step 1: Create a dictionary of student names and marks
students = {
    "Sourav": 76,
    "Priya": 92,
    "Alice": 85,
    "Nick": 89,
    "Ram": 95
}
# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")
# Step 3 and 4: Retrieve and display marks, or show a message if not found
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Student not found.")

''' Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

number = list(range(1, 11))
first_five = number[:5]
reversed_list = first_five[::-1]
print("Original list:", number)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)