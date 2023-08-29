# Hacked Game

[Hacked Game](https://pp3-hacked-game-932b8166abb0.herokuapp.com/) is a Python Terminal Application that is intended to educate people on the importance of strong passwords
It is comprised of

- A password strength checking tool
- An option to check if the users password is on the most hacked password list of 2022 [Source](https://parade.com/living/most-common-passwords)
- A password guessing game that uses the list of most hacked passwords in 2022
- An option to create strong passwords (and check the password strength simultaneously)

![Site Preview on desktop laptop tablet and mobile](assets/documentation/website_preview.jpg)

## How to use:

1. Go to https://pp3-hacked-game-932b8166abb0.herokuapp.com/
2. Wait for application to load

### Password Strength Checker:

1. From the main menu enter option "1" and press Enter
2. Type out your password (this field does not display the password typed) and press Enter
   - The application will then output "At a rate of 100 guesses per hour your password would take {time} to crack"
   - Passwords will then be deleted from memory
3. Press Enter to return to the main menu

### Is your password on the Hacked Password List?

1. From the main menu enter option "2" and press Enter
2. Type out your password (this field does not display the password typed) and press Enter

   - The application will then output either

     - The password entered is on the list
     - With additional feedback to change password

       ![Site feedback for password on list](assets/documentation/password_on_list.jpg)

   - The password entered is not on the list

     ![Site feedback for password not on list](assets/documentation/password_not_on_list.jpg)

3. Press Enter to return to the main menu

### Password Hacking Game:

1. From the main menu enter option "3" and press Enter
   - The menu will display 5 options
   - The game modes
   - View Leader Board
   - Exit to main menu
2. Enter the difficulty you wish the try:
   - "Easy"
   - "Difficult"
   - "Hard"
3. The game instructions will then print
4. Press Enter to continue to the game
5. The game will tell you the length of the password
6. Input your guess into the game and await feedback
7. Yellow feedback indicates that the characters are in the password but in the wrong location
   - ![Site feedback for correct character wrong location](assets/documentation/yellow_feedback_guess.jpg)
8. White feedback indicates that the characters are not in the password
   - ![Site feedback for character not in password](assets/documentation/white_feedback_guess.jpg)
9. Green feedback (u in the bellow screenshot) indicates that the characters are in the password and the correct location
   - ![Site feedback for correct character correct location](assets/documentation/green_feedback_guess.jpg)
10. If you guessed all the characters in the correct location you will win the game
    - ![Site feedback for winning the game](assets/documentation/win_feedback_game.jpg)
11. Enter your name to add your name to the leader-board, or select q to exit
12. If you get stuck you can enter help as an option to reveal the password character types
    - ![Site feedback for help function](assets/documentation/help_feedback_game.jpg)

### Password Hacking Game Leader-board

1. From the main menu enter option "3" and press Enter
   - The menu will display 5 options
   - The game modes
   - View Leader Board
   - Exit to main menu
2. Input 4 and press enter
3. You will then need to decide on the difficulty leaderboard to view
   - ![Site feedback for leader board options](assets/documentation/leader_board_game_options.jpg)
4. The desired leader board table will print (sorted lowest guesses to highest)
   - ![Leader board printed in terminal](assets/documentation/leader_board_game_preview.jpg)

### Password Generator

1. From the main menu enter option "4" and press Enter
2. Enter the length of the password greater than 1
   - 0 length passwords
   - Negative integer passwords
   - 1 length passwords will display an error
3. Copy the password from terminal
4. Press Enter to return to the main menu

Example Output:

- ![Password Generator output from terminal](assets/documentation/password_generator_output.jpg)
