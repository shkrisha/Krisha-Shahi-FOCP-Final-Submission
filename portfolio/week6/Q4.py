#Q)4)Computers are commonly used in encryption.
# A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string.
# Write, and test, a function that takes a string containing a message and "encrypts" it in this way.

def encrypt_user_message():
    try:
        user_message = input("Enter a message: ")
        if not user_message:
            return "Empty message."

        encrypted_message = user_message.replace(" ", "")[::-1]
        return encrypted_message
    except Exception as e:
        print(f"Error: {e}")

encrypted_message_result = encrypt_user_message()
print(f"Encrypted Message: {encrypted_message_result}")


