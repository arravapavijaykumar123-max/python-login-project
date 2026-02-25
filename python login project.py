# Registration and Login System
# -------------------------
# Username Validation
# -------------------------

def check_username(username):

    # username should not start with number or special character
    if username[0].isdigit() or not username[0].isalpha():
        print("Error: Username should start with a letter.")
        return False

    # username should have @
    if "@" not in username:
        print("Error: Username should contain @")
        return False

    # split username into two parts by @
    parts = username.split("@")
    before_at = parts[0]
    after_at = parts[1]

    # no dot immediately after @
    if after_at[0] == ".":
        print("Error: No dot allowed right after @")
        return False

    # there should be a dot after @
    if "." not in after_at:
        print("Error: Username should have a dot after @")
        return False

    return True


# -------------------------
# Password Validation
# -------------------------

def check_password(password):

    # length should be between 6 and 16
    if len(password) < 6 or len(password) > 16:
        print("Error: Password length should be between 6 and 16.")
        return False

    # check for uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
    if has_upper == False:
        print("Error: Password should have at least one uppercase letter.")
        return False

    # check for lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
    if has_lower == False:
        print("Error: Password should have at least one lowercase letter.")
        return False

    # check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    if has_digit == False:
        print("Error: Password should have at least one digit.")
        return False

    # check for special character
    special_characters = "!@#$%^&*(),.?:{}|<>"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
    if has_special == False:
        print("Error: Password should have at least one special character.")
        return False

    return True


# -------------------------
# Save user to file
# -------------------------

def save_user(username, password):
    file = open("users.txt", "a")
    file.write(username + ":" + password + "\n")
    file.close()


# -------------------------
# Load all users from file
# -------------------------

def load_users():
    users = {}
    try:
        file = open("users.txt", "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if ":" in line:
                parts = line.split(":")
                users[parts[0]] = parts[1]

    except FileNotFoundError:
        print("No users file found. Starting fresh.")

    return users


# -------------------------
# Update password in file
# -------------------------

def update_password(username, new_password):
    users = load_users()
    users[username] = new_password

    file = open("users.txt", "w")
    for u in users:
        file.write(u + ":" + users[u] + "\n")
    file.close()


# -------------------------
# Registration
# -------------------------

def register():
    print("\n====== REGISTRATION ======")

    while True:
        username = input("Enter your username (email): ")

        # check if username is valid
        if check_username(username) == False:
            continue

        # check if username already exists
        users = load_users()
        if username in users:
            print("This username already exists. Try another one.")
            continue

        # get password from user
        while True:
            password = input("Enter your password: ")

            if check_password(password) == False:
                continue
            else:
                break

        # save user details
        save_user(username, password)
        print("Registration Successful!")
        break


# -------------------------
# Forgot Password
# -------------------------

def forgot_password():
    print("\n====== FORGOT PASSWORD ======")

    users = load_users()
    username = input("Enter your username: ")

    # check if username exists
    if username not in users:
        print("Username not found. Please register first.")
        return

    # show current password
    print("Your current password is: " + users[username])

    choice = input("Do you want to set a new password? (yes/no): ")

    if choice == "yes":
        while True:
            new_password = input("Enter new password: ")
            if check_password(new_password) == False:
                continue
            else:
                update_password(username, new_password)
                print("Password updated successfully!")
                break


# -------------------------
# Login
# -------------------------

def login():
    print("\n====== LOGIN ======")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users = load_users()

    # check if username and password match
    if username in users and users[username] == password:
        print("Login Successful! Welcome " + username)

    else:
        print("Invalid username or password.")
        print("\nWhat do you want to do?")
        print("1. Register")
        print("2. Forgot Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            forgot_password()
        else:
            print("Exiting...")


# -------------------------
# Main Menu
# -------------------------

print("==============================")
print("  REGISTRATION & LOGIN SYSTEM ")
print("==============================")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank you! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")