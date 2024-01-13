#Q)5)Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. 
# Test both functions. (Google will find you the formulae).

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit_conversion(celsius):
    return (celsius * 9/5) + 32

# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius_conversion(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius_temperature = 25.0
fahrenheit_equivalent = celsius_to_fahrenheit_conversion(celsius_temperature)
converted_celsius = fahrenheit_to_celsius_conversion(fahrenheit_equivalent)

# Print the results
print(f"{celsius_temperature:.2f}°C is equivalent to {fahrenheit_equivalent:.2f}°F")
print(f"{fahrenheit_equivalent:.2f}°F is equivalent to {converted_celsius:.2f}°C")

