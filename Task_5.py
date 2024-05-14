def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    return True, "Password is valid."


while True:
    password = input("Create a password for your bank account: ")
    is_valid, message = validate_password(password)
    if is_valid:
        print(message, "\nYour password has been created successfully!!")
        break
    else:
        print("Invalid password.\n" + message + "\n")
