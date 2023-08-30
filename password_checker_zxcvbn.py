"""Used in option 1 and option 4 for password strength checking"""
from packages_global_vars import *


def password_checker(input_string):
    """Takes in a password (string), and returns
    a print statement on the time taken to crack password"""
    init(autoreset=True)

    if input_string == "" or len(input_string) == 0:
        print("Please enter a valid password")
        new_input = getpass("Enter the password to check: ")
        password_checker(new_input)
    elif input_string == "q":
        print("Exiting...")
        return
    else:
        # second includes "seconds" day includes "days" week includes "weeks"
        reset_colours = Style.RESET_ALL
        results = zxcvbn(input_string)
        results_in_time = results.get("crack_times_display").get(
            "online_throttling_100_per_hour")
        if ("second" in results_in_time
            or "minute" in results_in_time
            or "hour" in results_in_time
            or "day" in results_in_time
                or "week" in results_in_time):
            fore_ground = Fore.WHITE
            back_ground = Back.RED
            # month includes "months year includes "years"
        elif "month" in results_in_time:
            fore_ground = Fore.YELLOW
            back_ground = Back.BLACK
        elif "year" in results_in_time:
            fore_ground = Fore.GREEN
            back_ground = Back.WHITE
        else:
            fore_ground = Fore.GREEN
            back_ground = Back.WHITE

        print(f"At a rate of 100 guesses per hour your password would \
take {fore_ground}{back_ground}{results_in_time}{reset_colours} to crack")
        # removing password from memory
        del results
        del results_in_time
        print("")
        print("Deleting Password..")
        print("Your password has been deleted from memory..")
        input("Press enter to continue")
        os.system('cls||clear')
