#Q)3)Modify your "greetings" program so that the first letter of the name entered is always in uppercase with the rest in lowercase. 
# This should happen even if the user entered their name differently. 
# So if the user entered arthur, ARTHUR, or even arTHur the name should be displayed as Arthur.

# Prompt the user for their name
input_name = input("Hello, what is your name? ")

# Format the name with the first letter in uppercase and the rest in lowercase
formatted_name = input_name.capitalize()

# Print the greeting with the formatted name
print(f"Hello, {formatted_name}. Good to meet you!")
