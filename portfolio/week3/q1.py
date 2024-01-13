#Q)1)Modify your greeting program so that if the user does not enter a name (i.e. they just press enter), the program responds "Hello, Stranger!".
# Otherwise it should print a greeting with their name as before

# Prompt the user for their name
input_name = input("Hello, what is your name? ")

# Check if the user entered a name
if input_name:
    print(f"Hello, {input_name}. Good to meet you!")
else:
    print("Hello, Stranger!")

