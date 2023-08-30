import random
import os
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style, init
from zxcvbn import zxcvbn
from getpass import getpass
from tabulate import tabulate
from password_generator import PasswordGenerator

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hacked-passwords")
DATA = SHEET.worksheet("passwords")
PASSWORDS_DATA = DATA.col_values(1)
AMER_PASSWORDS = DATA.col_values(2)
leaderboard_sheet = SHEET.worksheet("leaderboard")


def generate_random_word(data):
    """Runs random choice 3 times and returns
    a random word. The random word is then sent
    to password_hacking_game function"""


    for i in range(3):
        word = random.choice(data)
        i += 1
    return word


def set_difficulty():
    """Creates an array of words based on the
    Google sheet data, to pass into generate_random_word function"""
    while True:
        print("This game has 3 modes")
        print("Easy")
        print("Difficult")
        print("Hard")
        print("press 4 to view the leaderboard")
        print("press q to exit")
        input_string = input(
            "What difficulty do you want to set?").lower().strip()
        new_array = []
        if input_string == "easy":
            for i in PASSWORDS_DATA:
                if len(i) <= 5:
                    new_array.append(i)
            return new_array
        elif input_string == "difficult":
            for i in PASSWORDS_DATA:
                if len(i) >= 6 and len(i) <= 8:
                    new_array.append(i)
            return new_array
        elif input_string == "hard":
            for i in PASSWORDS_DATA:
                if len(i) >= 9:
                    new_array.append(i)
            return new_array
        elif input_string == "4":
            get_leaderboard()
        elif input_string == "q":
            return False
        else:
            # clear terminal
            os.system('cls||clear')
            print("You have selected an incorrect option")


def password_hacking_game(random_word):
    """Main game logic
    inherits word from
    generate_random_word function"""
    # resets styling back to default
    init(autoreset=True)
    number_of_guesses = 0
    print(f"The password is {len(random_word)} characters long")
    CORRECT_LETTER = "\033[32m"
    LETTER_IN_WORD = "\033[33m"
    RESET_COLOURS = Style.RESET_ALL
    SPECIAL_CHARACTERS = "[@_!#$%^&*()<>?}{~:]"
    while True:
        print("")
        print("Enter help for assistance")
        correct = 0
        guess = input("\nWhat is your guess?")

        if guess == "q":
            return False

        elif guess == "help":
            help_array = []
            print("letter (upper) = uppercase")
            print("letter (lower) = lowercase")
            print("Number = 0-9")
            print(f"Special Character = {SPECIAL_CHARACTERS}")
            print("")
            print("Help reveal below:")
            for i, _ in enumerate(random_word):
                if random_word[i].isalpha():
                    if random_word[i].isupper():
                        help_array.append("Letter (upper)")
                    else:
                        help_array.append("Letter (lower)")
                elif random_word[i].isnumeric():
                    help_array.append("Number")
                elif random_word[i] in SPECIAL_CHARACTERS:
                    help_array.append("Special Character")

            for char in help_array:
                print(f"{char}, ", end="")
            print("")

        elif len(random_word) == len(guess):
            for i, _ in enumerate(random_word):
                if guess[i] == random_word[i]:
                    print(f"{CORRECT_LETTER}{guess[i]}{RESET_COLOURS}", end="")
                    correct += 1
                elif guess[i] in random_word:
                    print(f"{LETTER_IN_WORD}{guess[i]}{RESET_COLOURS}", end="")
                else:
                    print(f"{guess[i]}", end="")
            number_of_guesses += 1
            print("")
            print(f"Number of guesses = {number_of_guesses}")
            if correct == len(random_word):
                print(f"\nYou win with number of guesses {number_of_guesses}")
                print("Press Enter to continue")
                leaderboard(number_of_guesses, difficulty_for_leaderboard(
                    random_word))
                os.system('cls||clear')
                return False
        elif len(guess) < len(random_word):
            print("Your guess word is not long enough")
        elif len(guess) > len(random_word):
            print("Your guess word is too long")


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


def game():
    """Orders functions for the password_hacking_game"""
    password_array = set_difficulty()
    if password_array is False:
        return
    else:
        game_instructions()
        os.system('cls||clear')
        print(f"pa{password_array}")
        random_word = generate_random_word(password_array)
        password_hacking_game(random_word)


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


def leaderboard(number_of_tries, skill_level):
    """Validates user input against Google Sheets
    once valid appends the row to Google Sheets
    takes skill_level from set difficulty function"""
    while True:
        print("press q to skip")
        input_name = input(
            "Enter your Name to add to leaderboard").lower().strip()
        print(input_name)
        if input_name == "q":
            return False
        elif input_name == "" or len(input_name) == 0:
            print("Please enter a valid name")
        else:
            leaderboard_names = leaderboard_sheet.col_values(1)[1:]
            if input_name in leaderboard_names:
                print("name already exists")
            else:
                leaderboard_sheet.append_row(
                    [input_name, number_of_tries, skill_level])
                return False


def difficulty_for_leaderboard(correct_word):
    """Determines the difficulty of the user selection
    appends this data to the leaderboard in Google Sheets
    linked to function leaderboard function"""
    difficulty = ""
    if len(correct_word) <= 5:
        difficulty = "easy"
        return difficulty
    elif len(correct_word) >= 6 and len(correct_word) <= 8:
        difficulty = "difficult"
        return difficulty
    elif len(correct_word) >= 9:
        difficulty = "hard"
        return difficulty


def get_leaderboard():
    """Creates and sorts an array to pass into
    display_leaderboard function """
    running = True
    while running:
        print('Press 1 to see the "Easy" leaderboard')
        print('Press 2 to see the "Difficult" leaderboard')
        print('Press 3 to see the "Hard" leaderboard')
        print('Press q to return to the menu')
        selection = input("Enter your selection here: ").lower().strip()
        leaderboard_raw_data = leaderboard_sheet.get_all_values()[1:]
        updated_leaderboard_table = []
        if selection == "1":
            for row in leaderboard_raw_data:
                if row[2] == "easy":
                    updated_leaderboard_table.append(row)
            updated_leaderboard_table.sort(key=lambda num_guess: num_guess[1])
            display_leaderboard(updated_leaderboard_table)
            running = False
        elif selection == "2":
            for row in leaderboard_raw_data:
                if row[2] == "difficult":
                    updated_leaderboard_table.append(row)
            updated_leaderboard_table.sort(key=lambda num_guess: num_guess[1])
            display_leaderboard(updated_leaderboard_table)
            running = False
        elif selection == "3":
            for row in leaderboard_raw_data:
                if row[2] == "hard":
                    updated_leaderboard_table.append(row)
            updated_leaderboard_table.sort(key=lambda num_guess: num_guess[1])
            display_leaderboard(updated_leaderboard_table)
            running = False
        elif selection == "q":
            return
        else:
            print("Invalid option")


def display_leaderboard(raw_data):
    """Used to print the table takes in data from
    the get_leaderboard function"""
    row_headers = leaderboard_sheet.get_all_records()[0]
    print(tabulate(raw_data, headers=row_headers, tablefmt="fancy_grid"))
    input("Press enter to continue to main menu")
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


def game_instructions():
    os.system('cls||clear')
    init(autoreset=True)
    RESET_COLOURS = Style.RESET_ALL
    CORRECT_LETTER = "\033[32m"
    LETTER_IN_WORD = "\033[33m"
    correct_word = "Password12!"
    guessed = "Pass12!orxy"
    print("The objective of the game is to correctly guess the hacked\
password in the least amount of guesses")
    print("Your guess must be the same length as the password \
(You will be told the length of the password)")
    print("Incorrect length password tries and help commands \
will not be considered a guess")
    print(f"Correct character in the correct place will be \
highlighted in {CORRECT_LETTER}green {RESET_COLOURS}")
    print(f"The correct character in the wrong place will be \
highlighted in {LETTER_IN_WORD}yellow {RESET_COLOURS}")
    print(f"If the character is not in the word it will be\
printed as this white colour")
    print("Enter q as a guess at any point to exit the game")
    for i, _ in enumerate(correct_word):
        if guessed[i] == correct_word[i]:
            print(f"{CORRECT_LETTER}{guessed[i]}{RESET_COLOURS}", end="")
        elif guessed[i] in correct_word:
            print(f"{LETTER_IN_WORD}{guessed[i]}{RESET_COLOURS}", end="")
        else:
            print(f"{guessed[i]}", end="")

    help_array = []
    SPECIAL_CHARACTERS = "[@_!#$%^&*()<>?}{~:]"

    print("")
    print("")
    print("A help option is also available, enter help as you guess.")
    print("Help Menu")
    print("letter (upper) = uppercase")
    print("letter (lower) = lowercase")
    print("Number = 0-9")
    print(f"Special Character = {SPECIAL_CHARACTERS}")
    print("")
    print("Help Reveal:")
    for i, _ in enumerate(correct_word):
        if correct_word[i].isalpha():
            if correct_word[i].isupper():
                help_array.append("Letter (upper)")
            else:
                help_array.append("Letter (lower)")
        elif correct_word[i].isnumeric():
            help_array.append("Number")
        elif correct_word[i] in SPECIAL_CHARACTERS:
            help_array.append("Special Character")

    for char in help_array:
        print(f"{char}, ", end="")
    print("")
    print(f"Correct Word = {CORRECT_LETTER}{correct_word}")
    input("Press enter to continue")
    os.system('cls||clear')


def main():
    """ Main function calling other functions from modules"""
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
