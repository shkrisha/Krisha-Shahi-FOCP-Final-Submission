#Q)6)Write a program that decrypts messages encoded as above.

def decrypt_user_message(encrypted_message, interval_used):
    decrypted_message = ''.join(
        char if char.isalpha() else ''
        for i, char in enumerate(encrypted_message) if (i + 1) % (interval_used + 1) == 0
    )

    return decrypted_message

user_encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"
user_interval_used = 2
decrypted_message_result = decrypt_user_message(user_encrypted_message, user_interval_used)
print(f"Encrypted Message: {user_encrypted_message}")
print(f"Decrypted Message: {decrypted_message_result}")

