import gspread
from google.oauth2.service_account import Credentials
import random
from colorama import Fore, Back, Style, init
from zxcvbn import zxcvbn
from getpass import getpass
import os

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
        input_string = input("What difficulty do you want to set?").lower().strip()
        new_array = []
        if input_string == "easy":
            for i in PASSWORDS_DATA:
                if len(i) <=5:
                    new_array.append(i)
            return new_array
        elif input_string == "difficult":
            for i in PASSWORDS_DATA:
                if len(i) >=6 and len(i) <=8:
                    new_array.append(i)
            return new_array        
        elif input_string == "hard":
            for i in PASSWORDS_DATA:
                if len(i) >=9:
                    new_array.append(i)
            return new_array
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
           
    while number_of_guesses <= 5:
        print("")
        print("Enter help for assistance")
        correct = 0 
        guess = input("\nWhat is your guess?")
        
        if guess == "q":
            return False
        
        elif guess == "help":
            help_array = []
            for i in range(len(random_word)):
                if random_word[i].isalpha():
                    help_array.append("Letter")
                elif random_word[i].isnumeric():
                    help_array.append("Number")
                elif random_word[i] in SPECIAL_CHARACTERS:
                    help_array.append("Special Character")
            for char in help_array:
                print(f"{char} ", end="")
            print("")
        
        
        elif len(random_word) == len(guess):
            for i in range(0, len(random_word)):
                if guess[i] == random_word[i]:
                    print(f"{CORRECT_LETTER}{guess[i]}{RESET_COLOURS}", end="")
                    correct +=1
                elif guess[i] in random_word:
                    print(f"{LETTER_IN_WORD}{guess[i]}{RESET_COLOURS}",end="")
                else:
                    print(f"{guess[i]}", end="")
            number_of_guesses +=1
            if correct == len(random_word):
                print("\nYou win")
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
    if "second" in results_in_time or "minute" in results_in_time or "day" in results_in_time or "week" in results_in_time:
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

def game():
    password_array = set_difficulty()
    if password_array == False:
        return
    else:
        print(f"pa{password_array}")
        random_word = generate_random_word(password_array)
        password_hacking_game(random_word)
    
    

def main():
    while True:
        print("")
        print("Welcome")
        print("Press 1 to check your password strength")
        print("Press 2 to play the password hacking game")
        print("Press q to exit.")
        response = input("\n").lower().strip()
        
        if response == "1":
            password_checker(getpass("Enter the password to check: "))
        elif response == "2":
            game()
        elif response == "q":
            return False
main()

