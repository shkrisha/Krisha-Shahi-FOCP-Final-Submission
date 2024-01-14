#Q)3)Write and test a function that determines if a given integer is a prime number.
# A prime number is an integer greater than 1 that cannot be produced by multiplying two other integers.

def check_prime_from_user():
    try:
        user_input = int(input("Enter an integer: "))
        return user_input > 1 and all(user_input % i != 0 for i in range(2, int(user_input**0.5) + 1))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Example usage:
is_prime = check_prime_from_user()
if is_prime is not None:
    print(f"The entered number is {'prime' if is_prime else 'not prime'}.")

