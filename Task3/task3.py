import hashlib
import getpass
import os

def hash_password(password):
    # Use hashlib to securely hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def read_credentials_file(filename):
    if not os.path.exists(filename):
        # Create an empty file if it doesn't exist
        open(filename, 'w').close()
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def write_credentials_file(filename, lines):
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

def add_user(filename):
    new_username = input("Enter new username: ").strip()
    real_name = input("Enter real name: ").strip()
    password = hash_password(getpass.getpass("Enter password: ").strip())

    lines = read_credentials_file(filename)

    for line in lines:
        if line.startswith(new_username + ":"):
            print("Cannot add. Most likely username already exists.")
            return

    new_entry = f"{new_username}:{real_name}:{password}"
    lines.append(new_entry)
    write_credentials_file(filename, lines)

    print("User Created.")

def delete_user(filename):
    delete_username = input("Enter username: ").strip()

    lines = read_credentials_file(filename)

    for i, line in enumerate(lines):
        if line.startswith(delete_username + ":"):
            del lines[i]
            write_credentials_file(filename, lines)
            print("User Deleted.")
            return

    print("User not found. Nothing changed.")

def change_password(filename):
    username = input("User: ").strip()
    current_password = getpass.getpass("Current Password: ").strip()
    new_password = hash_password(getpass.getpass("New Password: ").strip())
    confirm_password = hash_password(getpass.getpass("Confirm: ").strip())

    lines = read_credentials_file(filename)

    for i, line in enumerate(lines):
        if line.startswith(username + ":"):
            stored_password = line.split(":")[2]

            if hash_password(current_password) == stored_password:
                if new_password == confirm_password:
                    lines[i] = f"{username}:{line.split(':')[1]}:{new_password}"
                    write_credentials_file(filename, lines)
                    print("Password changed.")
                else:
                    print("Passwords do not match. Nothing changed.")
                return
            else:
                print("Current password is invalid. Nothing changed.")
                return

    print("User not found. Nothing changed.")

def login(filename):
    username = input("User: ").strip()
    password = hash_password(getpass.getpass("Password: ").strip())

    lines = read_credentials_file(filename)

    for line in lines:
        if line.startswith(username + ":"):
            stored_password = line.split(":")[2]

            if password == stored_password:
                print("Access granted.")
                return
            else:
                print("Access denied.")
                return

    print("User not found. Access denied.")

if __name__ == "__main__":
    # Use the full path or adjust as needed
    filename = "credentials.txt"

    while True:
        print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_user(filename)
        elif choice == '2':
            delete_user(filename)
        elif choice == '3':
            change_password(filename)
        elif choice == '4':
            login(filename)
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
