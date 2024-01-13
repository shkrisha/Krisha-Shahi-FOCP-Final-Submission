#Q)3)Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.

# Prompt the user for a new password within length constraints
user_input_password1 = input("Enter a new password (8-12 characters): ")

# Check if the password meets the length constraint
if 8 <= len(user_input_password1) <= 12 and user_input_password1 == input("Enter the password again: "):
    print("Password Set")
else:
    print("Error: Password does not meet the length constraint or passwords do not match.")

