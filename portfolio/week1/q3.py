#Q)3)Over the summer, temperatures in Yorkshire reached 38.4C.
# Write a program that converts this value in Celsius to the equivalent temperature in Fahrenheit, and then displays both.

# Given temperature in Celsius
celsius_value = 38.4

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Convert Celsius to Fahrenheit
fahrenheit_value = celsius_to_fahrenheit(celsius_value)

# Display temperatures
print(f"Temperature in Celsius: {celsius_value}°C")
print(f"Temperature in Fahrenheit: {fahrenheit_value}°F")
