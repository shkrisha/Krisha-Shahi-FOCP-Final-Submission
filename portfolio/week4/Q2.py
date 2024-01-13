#Q)2)Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string. 
# Test the function with a short program.

# Define a function to count the number of uppercase and lowercase letters in a string
def count_case_characters(input_str):
    uppercase_count = sum(1 for char in input_str if char.isupper())
    lowercase_count = sum(1 for char in input_str if char.islower())
    return uppercase_count, lowercase_count

# Prompt the user to enter a string
user_input_string = input("Enter a string: ")

# Get the counts of uppercase and lowercase letters
upper_count, lower_count = count_case_characters(user_input_string)

# Print the results
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")


