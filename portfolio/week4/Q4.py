#Q)4)When processing data it is often useful to remove the last character from some input (it is often a newline).
# Write and test a function that takes a string parameter and returns it with the last character removed. 
# (If the string contains one or fewer characters, return it unchanged.)

# Define a function to remove the last character from a string (if it has more than one character)
def remove_last_char(input_str):
    return input_str[:-1] if len(input_str) > 1 else input_str

# Prompt the user to enter a string
user_input_string = input("Enter a string: ")

# Remove the last character from the string (if it has more than one character)
result_string = remove_last_char(user_input_string)

# Print the original and modified strings
print(f"Original string: {user_input_string}")
print(f"String with last character removed: {result_string}")

