#Q)2)Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively:
#Letters that appear in at least one of the two words.
#Letters that appear in both words.
#Letters that appear in either word, but not in both.
#Hint: These could all be done programmatically, but consider carefully what topic we have been discussing this week! Each function can be exactly one line

def get_letters_in_either(word1, word2):
    return sorted(set(word1.lower() + word2.lower()))

def get_letters_in_both(word1, word2):
    return sorted(set(char.lower() for char in word1 if char.isalpha()) & set(char.lower() for char in word2 if char.isalpha()))

def get_letters_in_either_not_both(word1, word2):
    return sorted(set(char.lower() for char in word1 if char.isalpha()) ^ set(char.lower() for char in word2 if char.isalpha()))

user_word1 = input("Enter the first word: ")
user_word2 = input("Enter the second word: ")

result1 = get_letters_in_either(user_word1, user_word2)
print(f"Letters in either word: {result1}")

result2 = get_letters_in_both(user_word1, user_word2)
print(f"Letters in both words: {result2}")

result3 = get_letters_in_either_not_both(user_word1, user_word2)
print(f"Letters in either word, but not in both: {result3}")

