"""Import all packages and check if password is on hacked list"""
from packages_global_vars import *


def password_in_list(input_string):
    """Takes in a password then verifies
    the data against Google Sheets data"""
    print("checking...")
    if input_string == "" or len(input_string) == 0:
        print("Please enter a valid password")
        new_input = getpass("Enter the password to check: ")
        password_in_list(new_input)
    elif input_string == "q":
        return
    else:
        reset_colours = Style.RESET_ALL
        on_list = False
        for password in PASSWORDS_DATA:
            if input_string == password:
                back_ground = Back.RED
                on_list = True
        for password in AMER_PASSWORDS:
            back_ground = Back.RED
            if input_string == password:
                on_list = True

        if on_list is True:
            print(f"{back_ground}Your password is on the list{reset_colours}")
            print(f"{back_ground}Please consider changing your\
password {reset_colours}")
        else:
            back_ground = Back.GREEN
            print(f"{back_ground}Your password is NOT on the list\
{reset_colours}")

        print("Deleting password")
        del input_string
        print("Your password has been deleted")
        input("Press enter to continue")
        os.system('cls||clear')
