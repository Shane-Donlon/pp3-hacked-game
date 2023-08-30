from packages_global_vars import *


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