#Q)2)Write a program that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit, like so:
#Enter a temperature in Celsius: 32.5
#32.5C is equivalent to 90.5F.

# Prompt the user to enter a temperature in Celsius
user_input_celsius = float(input("Enter a temperature in Celsius: "))

# Convert Celsius to Fahrenheit
temperature_fahrenheit = (9/5) * user_input_celsius + 32

# Display the result
print(f"{user_input_celsius}°C is equivalent to {temperature_fahrenheit:.1f}°F.")
