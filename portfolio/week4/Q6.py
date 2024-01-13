#Q)6)Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit. The input should be a number followed by a letter C. 
# The output should be in the same format.

# Prompt the user to enter the temperature in centigrade
user_input_str = input("Enter the temperature in centigrade (e.g., 25C): ")

# Extract the numeric part for temperature and the unit
temperature_celsius = float(user_input_str[:-1])
unit = user_input_str[-1].upper()

# Check the unit and perform conversion if it's in Celsius
if unit == 'C':
    # Convert Celsius to Fahrenheit
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    print(f"{temperature_celsius:.2f}C is equivalent to {temperature_fahrenheit:.2f}F")
else:
    print("Invalid input. Please use the format 'numberC'.")


