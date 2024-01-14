#Q)1)Write and test a function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string. 
# So, if the string is cheese, the list returned should be ['c', 'e', 'h', 's'].

def get_sorted_unique_letters(input_string):
    return sorted(set(char.lower() for char in input_string if char.isalpha()))

user_input_string = "cheese"
unique_letters_result = get_sorted_unique_letters(user_input_string)
print(f"Original String: {user_input_string}")
print(f"Unique Letters Sorted: {unique_letters_result}")

