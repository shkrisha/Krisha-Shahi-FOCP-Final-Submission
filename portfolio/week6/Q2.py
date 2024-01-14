#Q)2)Write and test a function that takes an integer as its parameter and returns the factors of that integer. 
# (A factor is an integer which can be multiplied by another to yield the original).

def get_factors_from_user():
    try:
        user_input = int(input("Enter an integer: "))
        factors = []
        for i in range(1, user_input + 1):
            if user_input % i == 0:
                factors.append(i)
        return factors
    except ValueError:
        print("Invalid input. Please enter an integer.")

factors_of_user_input = get_factors_from_user()
if factors_of_user_input:
    print(f"The factors are: {factors_of_user_input}")


