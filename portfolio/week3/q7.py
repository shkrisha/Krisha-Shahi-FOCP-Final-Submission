#Q)7)Modify your "Times Table" program so that the user enters the number of the table they require. This number should be between 0 and 12 inclusive.

# Prompt the user to enter the number for the times table (0-12)
user_input_table_number = int(input("Enter the number for the times table (0-12): "))

# Check if the entered number is within the valid range
if 0 <= user_input_table_number <= 12:
    # Display the requested times table
    for multiplier in range(13):
        result = multiplier * user_input_table_number
        print(f"{multiplier} x {user_input_table_number} = {result}")
else:
    print("Error: Please enter a number between 0 and 12.")

