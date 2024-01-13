#Q)7)Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum, and mean of the values.
#Hint: You should know there are built-in functions for max and min. If you hunt, you might also find one for the mean.
# Program to calculate max, min, and mean temperatures

# Program to calculate max, min, and mean temperatures

temperature_list = []

for i in range(6):
    user_input_str = input(f"Enter temperature {i + 1} in centigrade: ")

    if user_input_str[:-1].isdigit() and user_input_str.endswith('C'):
        temperature_list.append(float(user_input_str[:-1]))
    else:
        print(f"Ignored invalid input: {user_input_str}. Please use the format 'numberC'.")

if temperature_list:
    print(f"Maximum temperature: {max(temperature_list):.2f}C")
    print(f"Minimum temperature: {min(temperature_list):.2f}C")
    print(f"Mean temperature: {sum(temperature_list) / len(temperature_list):.2f}C")
else:
    print("No valid temperatures entered.")

