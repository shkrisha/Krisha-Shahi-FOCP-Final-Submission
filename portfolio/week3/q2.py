#Q)2)Write a program that simulates the way in which a user might choose a password.
#The program should prompt for a new password, and then prompt again. If the two passwords entered are the same the program should say "Password Set" or similar, otherwise it should report an error.

# Prompt the user for a new password
user_input_password1 = input("Enter a new password: ")

# Prompt the user to enter the password again
user_input_password2 = input("Enter the password again: ")

# Check if the two passwords entered are the same
if user_input_password1 == user_input_password2:
    print("Password Set")
else:
    print("Error: Passwords do not match. Please try again.")

