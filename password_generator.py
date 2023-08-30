from packages_global_vars import *
from password_checker import password_checker

def password_generator():
    """Used to generate password based on user input
    also uses the password_checker function
    to print the time to crack password"""
    while True:
        password_input = input("Enter the maximum length \
of the password in numbers: ")
        password_length = password_input.isnumeric()
        message = "Please enter positive integer values\
greater than 1 only or q to exit"
        if password_input == "q":
            print("Exiting...")
            return
        elif password_input == "0" or password_input == "1":
            print(message)
        elif password_length:
            password_input = int(password_input)
            if password_input > 40 or password_input <= 0:
                print("Password max length is set to 40 characters long")
            else:
                password = PasswordGenerator().non_duplicate_password(
                    password_input)
                print("Your password will be printed below")
                print(password)
                password_checker(password)
                return
        else:
            print(message)