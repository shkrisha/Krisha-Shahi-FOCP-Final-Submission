#Q)1)Functions are often used to validate input. Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise.
# Write a short program to test the function.

# Define a function to check if the integer is in the range 0 to 100 (inclusive)
def is_in_range_check(number):
    return 0 <= number <= 100

# Prompt the user to enter an integer
user_input_integer = int(input("Enter an integer: "))

# Print whether the integer is in the specified range
print(f"{user_input_integer} is {'in' if is_in_range_check(user_input_integer) else 'outside'} the range 0 to 100.")

