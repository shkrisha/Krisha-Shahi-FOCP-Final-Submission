#Q)8)Modify the "Times Table" again so that the user still enters the number of the table, but if this number is negative the table is printed backwards. So entering "-7" would produce the Seven Times Table starting at "12 times" down to "0 times".

# Prompt the user to enter the number for the times table (-12 to 12)
user_input_table_number = int(input("Enter the number for the times table (-12 to 12): "))

# Check if the entered number is within the valid range
if -12 <= user_input_table_number <= 12:
    # Determine the step for the loop based on the sign of the table number
    step = -1 if user_input_table_number < 0 else 1
    
    # Display the requested times table (backward or forward)
    for i in range(12 * step, (12 + step * 1), step):
        result = i * user_input_table_number
        print(f"{i * step} x {user_input_table_number} = {result}")
else:
    print("Error: Please enter a number between -12 and 12.")

