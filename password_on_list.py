from packages_global_vars import *


def password_in_list(input_string):
    """Takes in a password then verifies
    the data against Google Sheets data"""
    print("checking...")
    if input_string == "" or len(input_string) == 0:
        print("Please enter a valid password")
        new_input = getpass("Enter the password to check: ")
        password_in_list(new_input)
    else:
        RESET_COLOURS = Style.RESET_ALL
        on_list = False
        for password in PASSWORDS_DATA:
            if input_string == password:
                BACKGROUND = Back.RED
                on_list = True
        for password in AMER_PASSWORDS:
            BACKGROUND = Back.RED
            if input_string == password:
                on_list = True

        if on_list is True:
            print(f"{BACKGROUND}Your password is on the list{RESET_COLOURS}")
            print(f"{BACKGROUND}Please consider changing your\
password {RESET_COLOURS}")
        else:
            BACKGROUND = Back.GREEN
            print(f"{BACKGROUND}Your password is NOT on the list\
{RESET_COLOURS}")

    print("Deleting password")
    del input_string
    print("Your password has been deleted")
    input("Press enter to continue")
    os.system('cls||clear')
