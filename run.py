from packages_global_vars import *
from game import *






def password_checker(input_string):
    """Takes in a password (string), and returns
    a print statement on the time taken to crack password"""
    init(autoreset=True)

    if input_string == "" or len(input_string) == 0:
        print("Please enter a valid password")
        new_input = getpass("Enter the password to check: ")
        password_checker(new_input)
    else:
        # second includes "seconds" day includes "days" week includes "weeks"
        RESET_COLOURS = Style.RESET_ALL
        results = zxcvbn(input_string)
        results_in_time = results.get("crack_times_display").get(
            "online_throttling_100_per_hour")
        if ("second" in results_in_time
            or "minute" in results_in_time
            or "hour" in results_in_time
            or "day" in results_in_time
                or "week" in results_in_time):
            FOREGROUND = Fore.WHITE
            BACKGROUND = Back.RED
            # month includes "months year includes "years"
        elif "month" in results_in_time:
            FOREGROUND = Fore.YELLOW
            BACKGROUND = Back.BLACK
        elif "year" in results_in_time:
            FOREGROUND = Fore.GREEN
            BACKGROUND = Back.WHITE
        else:
            FOREGROUND = Fore.GREEN
            BACKGROUND = Back.WHITE

        print(f"At a rate of 100 guesses per hour your password would \
take {FOREGROUND}{BACKGROUND}{results_in_time}{RESET_COLOURS} to crack")
        # removing password from memory
        del results
        del results_in_time
        print("")
        print("Deleting Password..")
        print("Your password has been deleted from memory..")
        input("Press enter to continue")
        os.system('cls||clear')





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
