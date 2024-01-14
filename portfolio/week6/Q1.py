#Q)1)Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).
#Hint: This is in many ways a trick question. Think!

def get_binary_representation_from_user():
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input < 0:
            raise ValueError("Input must be a positive integer.")
        elif user_input == 0:
            return "0b0"
        else:
            return bin(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

binary_representation = get_binary_representation_from_user()
if binary_representation:
    print(f"The binary representation is: {binary_representation}")


