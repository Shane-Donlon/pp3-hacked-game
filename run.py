from packages_global_vars import *
from game import *
from password_generator import *
from password_on_list import *
from password_checker_zxcvbn import *












def main():
    while True:
        print("")
        print("Welcome")
        print("Press 1 to check your password strength")
        print(
            "Press 2 to check your password against the hacked password list")
        print("Press 3 to play the password hacking game")
        print("Press 4 to create a new password")
        print("Press q to exit.")
        response = input("\n").lower().strip()

        if response == "1":
            password_checker(getpass("Enter the password to check: "))
        elif response == "2":
            password_in_list(getpass("Enter the password to check: "))
        elif response == "3":
            game()
        elif response == "4":
            password_generator()
        elif response == "q":
            return False
        else:
            print("You have selected an incorrect option")


if __name__ == "__main__":
    main()
