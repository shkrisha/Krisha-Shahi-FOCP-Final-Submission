#Q)8)Modify the previous program so that it can process any number of values. The input terminates when the user just pressed "Enter" at the prompt rather than entering a value.

# Program to calculate max, min, and mean temperatures for any number of values

temperature_list = []

while (user_input_str := input("Enter temperature in centigrade (press Enter to finish): ").strip()):
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

