from packages_global_vars import *


def game_instructions():
    """ Prints game instructions for user"""
    os.system('cls||clear')
    init(autoreset=True)
    reset_colours = Style.RESET_ALL
    correct_letter = "\033[32m"
    letter_in_word = "\033[33m"
    correct_word = "Password12!"
    guessed = "Pass12!orxy"
    print("The objective of the game is to correctly guess the hacked\
password in the least amount of guesses")
    print("Your guess must be the same length as the password \
(You will be told the length of the password)")
    print("Incorrect length password tries and help commands \
will not be considered a guess")
    print(f"Correct character in the correct place will be \
highlighted in {correct_letter}green {reset_colours}")
    print(f"The correct character in the wrong place will be \
highlighted in {letter_in_word}yellow {reset_colours}")
    print("If the character is not in the word it will be\
printed as this white colour")
    print("Enter q as a guess at any point to exit the game")
    for i, _ in enumerate(correct_word):
        if guessed[i] == correct_word[i]:
            print(f"{correct_letter}{guessed[i]}{reset_colours}", end="")
        elif guessed[i] in correct_word:
            print(f"{letter_in_word}{guessed[i]}{reset_colours}", end="")
        else:
            print(f"{guessed[i]}", end="")

    help_array = []
    special_characters = "[@_!#$%^&*()<>?}{~:]"

    print("")
    print("")
    print("A help option is also available, enter help as you guess.")
    print("Help Menu")
    print("letter (upper) = uppercase")
    print("letter (lower) = lowercase")
    print("Number = 0-9")
    print(f"Special Character = {special_characters}")
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
        elif correct_word[i] in special_characters:
            help_array.append("Special Character")

    for char in help_array:
        print(f"{char}, ", end="")
    print("")
    print(f"Correct Word = {correct_letter}{correct_word}")
    input("Press enter to continue")
    os.system('cls||clear')


def set_difficulty():
    """Creates an array of words based on the
    Google sheet data, to pass into generate_random_word function"""
    while True:
        print("This game has 3 modes")
        print("Easy")
        print("Difficult")
        print("Hard")
        print("press 4 to view the leader board")
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


def generate_random_word(data):
    """Runs random choice 3 times and returns
    a random word. The random word is then sent
    to password_hacking_game function"""

    for i in range(3):
        word = random.choice(data)
        i += 1
    return word


def password_hacking_game(random_word):
    """Main game logic
    inherits word from
    generate_random_word function"""
    # resets styling back to default
    init(autoreset=True)
    number_of_guesses = 0
    print(f"The password is {len(random_word)} characters long")
    correct_letter = Back.GREEN
    letter_in_word = Back.YELLOW
    reset_colours = Style.RESET_ALL
    special_characters = "[@_!#$%^&*()<>?}{~:]"
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
            print(f"Special Character = {special_characters}")
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
                elif random_word[i] in special_characters:
                    help_array.append("Special Character")

            for char in help_array:
                print(f"{char}, ", end="")
            print("")

        elif len(random_word) == len(guess):
            for i, _ in enumerate(random_word):
                if guess[i] == random_word[i]:
                    print(f"{correct_letter}{guess[i]}{reset_colours}", end="")
                    correct += 1
                elif guess[i] in random_word:
                    print(f"{letter_in_word}{guess[i]}{reset_colours}", end="")
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


def game():
    """Orders functions for the password_hacking_game"""
    password_array = set_difficulty()
    if password_array is False:
        return
    else:
        game_instructions()
        os.system('cls||clear')
        random_word = generate_random_word(password_array)
        password_hacking_game(random_word)


def leaderboard(number_of_tries, skill_level):
    """Validates user input against Google Sheets
    once valid appends the row to Google Sheets
    takes skill_level from set difficulty function"""
    while True:
        print("press q to skip")
        input_name = input(
            "Enter your Name to add to leader board").lower().strip()
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
        print('Press 1 to see the "Easy" leader board')
        print('Press 2 to see the "Difficult" leader board')
        print('Press 3 to see the "Hard" leader board')
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
