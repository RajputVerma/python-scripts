'''Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist'''
try:
    file1 = open("sample.txt", "r")
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: sample.txt file not found.")
'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
# Step 1: Write to the file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt")

# Step 2: Append to the file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended")

# Step 3: Read and display the final content
print("\nFinal content of output.txt: ")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

