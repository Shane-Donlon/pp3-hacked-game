import gspread
from google.oauth2.service_account import Credentials
import random
from colorama import Fore, Back, Style, init
from zxcvbn import zxcvbn
from getpass import getpass
import os
from tabulate import tabulate


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
    an array of characters in that word
    EG ['1', 'g', 'd', 'D', 'f', 'g', 'd']"""

    i = 0
    while i < 3:
        word = random.choice(data)
        i += 1
    return word


def set_difficulty():
    while True:
        # clear terminal
        os.system('cls||clear')
        print("This game has 3 modes")
        print("Easy")
        print("Difficult")
        print("Hard")
        print("press 4 to view the leaderboard")
        input_string = input("What difficulty do you want to set?").lower().strip()
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
    # resets styling back to default
    init(autoreset=True)
    number_of_guesses = 0
    print(f"The password is {len(random_word)} characters long")
    CORRECT_LETTER = "\033[32m"
    LETTER_IN_WORD = "\033[33m"
    RESET_COLOURS = "\033[0m"
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
            for i in range(len(random_word)):
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
            for i in range(0, len(random_word)):
                if guess[i] == random_word[i]:
                    print(f"{CORRECT_LETTER}{guess[i]}{RESET_COLOURS}", end="")
                    correct += 1
                elif guess[i] in random_word:
                    print(f"{LETTER_IN_WORD}{guess[i]}{RESET_COLOURS}", end="")
                else:
                    print(f"{guess[i]}", end="")
            number_of_guesses += 1
            if correct == len(random_word):
                print(f"\nYou win with number of guesses {number_of_guesses}")
                print("Press Enter to continue")
                leaderboard(number_of_guesses, difficulty_for_leaderboard(random_word))
                os.system('cls||clear')
                return False
        elif len(guess) < len(random_word):
            print("Your guess word is not long enough")
        elif len(guess) > len(random_word):
            print("Your guess word is too long")


def password_checker(input_string):
    init(autoreset=True)
    RESET_COLOURS = "\033[0m"
    results = zxcvbn(input_string)
    results_in_time = results.get("crack_times_display").get("online_throttling_100_per_hour")
    # second includes "seconds" day includes "days" week includes "weeks"
    if "second" in results_in_time or "minute" in results_in_time or "hour" in results_in_time or "day" in results_in_time or "week" in results_in_time:
        FOREGROUND = Fore.WHITE
        BACKGROUND = Back.RED
        # month includes "months year includes "years"
    elif "month" in results_in_time:
        FOREGROUND = Fore.YELLOW
        BACKGROUND = Back.WHITE
    elif "year" in results_in_time:
        FOREGROUND = Fore.GREEN
        BACKGROUND = Back.WHITE
    else:
        FOREGROUND = Fore.GREEN
        BACKGROUND = Back.WHITE

    print(f"At a rate of 100 guesses per hour your password would take {FOREGROUND}{BACKGROUND}{results_in_time}{RESET_COLOURS} to crack")

    # removing password from memory
    del results
    del results_in_time
    print("")
    print("Deleting Password..")
    print("Your password has been deleted from memory..")
    input("Press enter to continue")


def game():
    password_array = set_difficulty()
    if password_array == False:
        return
    else:
        print(f"pa{password_array}")
        random_word = generate_random_word(password_array)
        password_hacking_game(random_word)


def password_in_list(input_string):
    print("checking...")
    on_list = False
    for password in PASSWORDS_DATA:
        if input_string == password:
            on_list = True

    for password in AMER_PASSWORDS:
        if input_string == password:
            on_list = True

    if on_list == True:
        print(f"Your password is on the list")
        print(f"Please consider changing your password")
    else:
        print(f"Your password is NOT on the list")
        input("Press enter to continue")

    print("Deleting password")
    del input_string
    print("Your password has been deleted")
    input("Press enter to continue")


def leaderboard(number_of_tries, skill_level):
    while True:
        print("press q to skip")
        input_name = input("Enter your Name to add to leaderboard").lower().strip()
        print(input_name)
        if input_name == "q":
            return False
        else:
            leaderboard_names = leaderboard_sheet.col_values(1)[1:]
            if input_name in leaderboard_names:
                print("name already exists")
            else:
                leaderboard_sheet.append_row([input_name, number_of_tries, skill_level])
                return False


def difficulty_for_leaderboard(correct_word):
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
    running = True
    while running:
        print('Press 1 to see the "Easy" leaderboard')
        print('Press 2 to see the "Difficult" leaderboard')
        print('Press 3 to see the "Hard" leaderboard')
        selection = input("Enter your selection here: ").lower().strip()
        leaderboard_raw_data = leaderboard_sheet.get_all_values()[1:]
        updated_leaderboard_table = []
        if selection == "1":
            for row in leaderboard_raw_data:
                if row[2] == "easy":
                    updated_leaderboard_table.append(row)
            running = False
        elif selection == "2":
            for row in leaderboard_raw_data:
                if row[2] == "difficult":
                    updated_leaderboard_table.append(row)
            running = False
        elif selection == "3":
            for row in leaderboard_raw_data:
                if row[2] == "hard":
                    updated_leaderboard_table.append(row)
            running = False
        else:
            print("Invalid option")
        updated_leaderboard_table.sort(key=lambda num_guess: num_guess[1])
        display_leaderboard(updated_leaderboard_table)


def display_leaderboard(raw_data):
    row_headers = leaderboard_sheet.get_all_records()[0]
    print(tabulate(raw_data, headers=row_headers, tablefmt="fancy_grid"))
    input("Press enter to continue to main menu")


def main():
    while True:
        print("")
        print("Welcome")
        print("Press 1 to check your password strength")
        print("Press 2 to check your password against the hacked password list")
        print("Press 3 to play the password hacking game")
        print("Press q to exit.")
        response = input("\n").lower().strip()

        if response == "1":
            password_checker(getpass("Enter the password to check: "))
        elif response == "2":
            password_in_list(getpass("Enter the password to check: "))
        elif response == "3":
            game()
        elif response == "q":
            return False
main()
