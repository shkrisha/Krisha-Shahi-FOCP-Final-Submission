#Q)4)Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus:
#BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Define a list of common passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Prompt the user for a new password within length constraints
user_input_password1 = input("Enter a new password (8-12 characters): ")

# Check if the password meets the length constraint and is not in the list of common passwords
if 8 <= len(user_input_password1) <= 12 and user_input_password1 not in BAD_PASSWORDS and user_input_password1 == input("Enter the password again: "):
    print("Password Set")
else:
    print("Error: Password does not meet the constraints.")
