#Q)5)Modify your program a final time so that it executes until the user successfully chooses a password. That is, if the password chosen fails any of the checks, the program should return to asking for the password the first time.

# Define a list of common passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    # Prompt the user for a new password within length constraints
    user_input_password = input("Enter a new password (8-12 characters): ")
    
    # Check if the password meets the length constraint and is not in the list of common passwords
    if 8 <= len(user_input_password) <= 12 and user_input_password not in BAD_PASSWORDS and user_input_password == input("Enter the password again: "):
        print("Password Set")
        break
    else:
        print("Error: Password does not meet the constraints. Please try again.")


