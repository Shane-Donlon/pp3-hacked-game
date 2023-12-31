# Hacked Game

[Hacked Game](https://pp3-hacked-game-932b8166abb0.herokuapp.com/) is a Python Terminal Application that is intended to educate people on the importance of strong passwords
It is comprised of

- A password strength checking tool
- An option to check if the users password is on the most hacked password list of 2022 [Source](https://parade.com/living/most-common-passwords)
- A password guessing game that uses the list of most hacked passwords in 2022
- An option to create strong passwords (and check the password strength simultaneously)

![Site Preview on desktop laptop tablet and mobile](assets/documentation/website_preview.jpg)

## User Stories

- As a user I want a site where I can check the strength of my password
- As a user I want a site where I can verify my password against common passwords
- As a user I want to play a game to educate me on using weak passwords
- As a user I want to play a game to educate me on common passwords
- As a user I want to be able to create strong passwords and verify the strength of the new password generated

## How to use & Features:

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

   ![Site feedback for correct character wrong location](assets/documentation/yellow_feedback_guess.jpg)

8. White feedback indicates that the characters are not in the password

   ![Site feedback for character not in password](assets/documentation/white_feedback_guess.jpg)

9. Green feedback (u in the bellow screenshot) indicates that the characters are in the password and the correct location

   ![Site feedback for correct character correct location](assets/documentation/green_feedback_guess.jpg)

10. If you guessed all the characters in the correct location you will win the game

    ![Site feedback for winning the game](assets/documentation/win_feedback_game.jpg)

11. Enter your name to add your name to the leader-board, or select q to exit
12. If you get stuck you can enter help as an option to reveal the password character types

    ![Site feedback for help function](assets/documentation/help_feedback_game.jpg)

### Password Hacking Game Leader-board

1. From the main menu enter option "3" and press Enter
   - The menu will display 5 options
   - The game modes
   - View Leader Board
   - Exit to main menu
2. Input 4 and press enter
3. You will then need to decide on the difficulty leader board to view

   ![Site feedback for leader board options](assets/documentation/leader_board_game_options.jpg)

4. The desired leader board table will print (sorted lowest guesses to highest)

   ![Leader board printed in terminal](assets/documentation/leader_board_game_preview.jpg)

### Password Generator

1. From the main menu enter option "4" and press Enter
2. Enter the length of the password greater than 1
   - 0 length passwords
   - Negative integer passwords
   - 1 length passwords will display an error
3. Copy the password from terminal
4. Press Enter to return to the main menu

Example Output:

![Password Generator output from terminal](assets/documentation/password_generator_output.jpg)

## Technologies used:

### Languages:

- [Python](https://www.python.org/) The main language used in the terminal application
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) Used in the template to run the terminal
- [HTML](https://en.wikipedia.org/wiki/HTML) used in the template to present the terminal

### Libraries and packages used:

- [gspread](https://github.com/burnash/gspread) Google API for GoogleSheets
- [google.oauth2.service_account](https://developers.google.com/identity/protocols/oauth2/service-account) Account used to share the worksheets with
- [colorama](https://pypi.org/project/colorama/) used to add color for visual feedback
- [zxcvbn](https://pypi.org/project/zxcvbn/) used for password strength
- [getpass](https://docs.python.org/3/library/getpass.html) used to hide the password input
- [tabulate](https://pypi.org/project/tabulate/) Used to create the leader board tables
- [random password generator](https://pypi.org/project/random-password-generator/) used to generate random passwords

### Other Tools:

- [GitHub](https://github.com/): Used to host the application source code.
- [VSCode](https://code.visualstudio.com/) Visual Studio Code: used to edit the application source code.
- [Heroku](https://www.heroku.com/): Used to host the application
- [LucidChart](https://www.lucidchart.com/pages/) Used for diagrams

## Workflows

### Main menu

![Main Menu Workflow](assets/documentation/main_menu_workflow.jpg)

### Password Strength Checker

![Password Strength Workflow](assets/documentation/password_strength_checker_workflow.jpg)

### Password On List

![Password on password list Workflow](assets/documentation/password_list_workflow.jpg)

### Main Game

![main Game Workflow](assets/documentation/main_game_workflow.jpg)

### Leaderboard

![Leader Board Workflow](assets/documentation/leader_board_workflow.jpg)

### Password Generator

![Password Generator Workflow](assets/documentation/create_password_workflow.jpg)

## Testing

### Automated Testing

No errors found
- run.py module

![Python Linter Results for run.py file](assets/documentation/pep8_run_file.jpg)

- password_on_list.py module

![Python Linter Results for password_on_list.py file](assets/documentation/pep8_packages_file.jpg)

- password_checker_zxcvbn.py module

![Python Linter Results for password_on_password_checker_zxcvbn.py file](assets/documentation/pep8_password_checker_file.jpg)

- password_global_vars.py module
![Python Linter Results for password_on_password_global_vars.py file](assets/documentation/pep8_global_vars_file.jpg)

- generating_password.py module
![Python Linter Results for password_on_generating_password.py  file](assets/documentation/pep8_generating_file.jpg)

- game.py module
![Python Linter Results for password_on_generating_password.py  file](assets/documentation/pep8_game_file.jpg)


### Manual Testing

Command Prompt was used to run the application locally, and updates were tested again after deployment to Heroku


<table>
<thead>
  <tr>
    <th>Testing Description</th>
    <th>Expected Action</th>
    <th>Actual Output</th>
    <th>Result</th>

  </tr>
</thead>
<tbody>
  <tr>
    <td>Main Menu Loads</td>
    <td>User is presented with menu</td>
    <td>User is presented with menu</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Main Menu Option 1</td>
    <td>User is presented with password strength checking tool</td>
    <td>User is presented with password strength checking tool</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Main Menu Option 2</td>
    <td>User is presented with checking password against password list</td>
    <td>User is presented with checking password against password list</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Main Menu Option 3</td>
    <td>User is presented with a game</td>
    <td>User is presented with a game</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Main Menu Option 4</td>
    <td>User can create a new password</td>
    <td>User can create a new password</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Main Menu Option Q</td>
    <td>Application ends</td>
    <td>Application ends</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>All other input</td>
    <td>Presents error and presents menu</td>
    <td>Presents error and presents menu</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Strength</td>
    <td>User inputs a correct password to verify </td>
    <td>Password is verified with time to crack</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Strength</td>
    <td>User inputs a 0 length password</td>
    <td>User is presented with error and asked to enter a correct password</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password List</td>
    <td>User inputs a correct on the list</td>
    <td>User is informed password is on the list</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password List</td>
    <td>User inputs a password not on the list</td>
    <td>User is informed password is not on the list</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password List</td>
    <td>User inputs a 0 length password</td>
    <td>User is presented with error and asked to enter a correct password</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game</td>
    <td>User is presented with Difficulty menu</td>
    <td>User is presented with Difficulty menu</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game</td>
    <td>user inputs easy</td>
    <td>Easy mode loads</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game</td>
    <td>user inputs difficult</td>
    <td>Difficult mode loads</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game</td>
    <td>user inputs hard</td>
    <td>Hard mode loads</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game</td>
    <td>user inputs 4</td>
    <td>user is presented with leader board options</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game Menu</td>
    <td>User inputs invalid option</td>
    <td>User presented with error and menu options</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game leader board</td>
    <td>user inputs 1</td>
    <td>Easy Leader board is presented</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game leader board</td>
    <td>user inputs 2</td>
    <td>Difficult Leader board is presented</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game leader board</td>
    <td>user inputs 3</td>
    <td>Hard Leader board is presented</td>
    <td>Confirmed</td>
  </tr>   
  <tr>
    <td>Password Game leader board</td>
    <td>user inputs q</td>
    <td>User exists current menu</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game Easy</td>
    <td>User is presented with game instructions</td>
    <td>User is presented with game instructions</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Difficult</td>
    <td>User is presented with game instructions</td>
    <td>User is presented with game instructions</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Hard</td>
    <td>User is presented with game instructions</td>
    <td>User is presented with game instructions</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Easy</td>
    <td>User inputs guess q</td>
    <td>Game ends</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Difficult</td>
    <td>User inputs guess q</td>
    <td>Game ends</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Hard</td>
    <td>User inputs guess q</td>
    <td>Game ends</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Easy</td>
    <td>User inputs guess help</td>
    <td>User is presented with help options (as above)</td>
    <td>Confirmed</td>
  </tr>   
  <tr>
    <td>Password Game Difficult</td>
    <td>User inputs guess help</td>
    <td>User is presented with help options (as above)</td>
    <td>Confirmed</td>
  </tr>   
  <tr>
    <td>Password Game Hard</td>
    <td>User inputs guess help</td>
    <td>User is presented with help options (as above)</td>
    <td>Confirmed</td>
  </tr>   
  <tr>
    <td>Password Game Easy</td>
    <td>User inputs a guess too short</td>
    <td>Error to inform user of this appears</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Easy</td>
    <td>User inputs a guess too long</td>
    <td>Error to inform user of this appears</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Easy</td>
    <td>Guess is the correct length with incorrect characters</td>
    <td>Printed guess characters in default white</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Easy</td>
    <td>Guess is the correct length with correct letters in wrong place</td>
    <td>Printed guess characters in yellow</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Easy</td>
    <td>Guess is the correct length with correct letters in correct place</td>
    <td>Printed guess characters in green</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game Difficult</td>
    <td>User inputs a guess too short</td>
    <td>Error to inform user of this appears</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Difficult</td>
    <td>User inputs a guess too long</td>
    <td>Error to inform user of this appears</td>
    <td>Confirmed</td>
  </tr> 
  <tr>
    <td>Password Game Difficult</td>
    <td>Guess is the correct length with incorrect characters</td>
    <td>Printed guess characters in default white</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Difficult</td>
    <td>Guess is the correct length with correct letters in wrong place</td>
    <td>Printed guess characters in yellow</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Difficult</td>
    <td>Guess is the correct length with correct letters in correct place</td>
    <td>Printed guess characters in green</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game Hard</td>
    <td>User inputs a guess too short</td>
    <td>Error to inform user of this appears</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Hard</td>
    <td>User inputs a guess too long</td>
    <td>Error to inform user of this appears</td>
    <td>Confirmed</td>
  </tr> 
  <tr>
    <td>Password Game Hard</td>
    <td>Guess is the correct length with incorrect characters</td>
    <td>Printed guess characters in default white</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Hard</td>
    <td>Guess is the correct length with correct letters in wrong place</td>
    <td>Printed guess characters in yellow</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game Hard</td>
    <td>Guess is the correct length with correct letters in correct place</td>
    <td>Printed guess characters in green</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game User wins Easy</td>
    <td>User has guessed the correct word</td>
    <td>Whole word appears in green</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User wins Difficult</td>
    <td>User has guessed the correct word</td>
    <td>Whole word appears in green</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User wins Hard</td>
    <td>User has guessed the correct word</td>
    <td>Whole word appears in green</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Easy</td>
    <td>User is asked to enter name</td>
    <td>User is asked to enter name</td>
    <td>Confirmed</td>
  </tr> 
    <tr>
    <td>Password Game User Wins Easy</td>
    <td>User enters a 0 length name</td>
    <td>Error message is displayed and asked for a name</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game User Wins Easy</td>
    <td>User enters q as name</td>
    <td>User returns to menu skipping leader board</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Easy</td>
    <td>User enters a legitimate name not already on list</td>
    <td>leader board is updated</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Easy</td>
    <td>User enters a legitimate name already on list</td>
    <td>error stating name is already on list appears and asked for a new name</td>
    <td>Confirmed</td>
  </tr>

<tr>
    <td>Password Game User Wins Difficult</td>
    <td>User is asked to enter name</td>
    <td>User is asked to enter name</td>
    <td>Confirmed</td>
  </tr> 
    <tr>
    <td>Password Game User Wins Difficult</td>
    <td>User enters a 0 length name</td>
    <td>Error message is displayed and asked for a name</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game User Wins Difficult</td>
    <td>User enters q as name</td>
    <td>User returns to menu skipping leader board</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Difficult</td>
    <td>User enters a legitimate name not already on list</td>
    <td>leader board is updated</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Difficult</td>
    <td>User enters a legitimate name already on list</td>
    <td>error stating name is already on list appears and asked for a new name</td>
    <td>Confirmed</td>
  </tr>  
<tr>
    <td>Password Game User Wins Hard</td>
    <td>User is asked to enter name</td>
    <td>User is asked to enter name</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Hard</td>
    <td>User enters q as name</td>
    <td>User returns to menu skipping leader board</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Hard</td>
    <td>User enters a legitimate name not already on list</td>
    <td>leader board is updated</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Password Game User Wins Hard</td>
    <td>User enters a 0 length name</td>
    <td>Error message is displayed and asked for a name</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Game User Wins Hard</td>
    <td>User enters a legitimate name already on list</td>
    <td>error stating name is already on list appears and asked for a new name</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Generator</td>
    <td>User enters a positive integer between 2 and 40</td>
    <td>User is presented with password and password strength</td>
    <td>Confirmed</td>
  </tr>  
  <tr>
    <td>Password Generator</td>
    <td>User enters negative integer</td>
    <td>User is presented with error and instructions</td>
    <td>Confirmed</td>
  </tr>   
  <tr>
    <td>Password Generator</td>
    <td>User enters any number above 40</td>
    <td>User is presented with error and instructions</td>
    <td>Confirmed</td>
  </tr>
   <tr>
    <td>Password Generator</td>
    <td>User enters a 0 or 1 length password</td>
    <td>User is presented with error and instructions</td>
    <td>Confirmed</td>
    </tr>
   <tr>
    <td>Google Sheets data reads</td>
    <td>Password List reads from Google Sheets</td>
    <td>Password options are in the game</td>
    <td>Confirmed</td>
    </tr>
   <tr>
    <td>Google Sheets data writes</td>
    <td>Leader board stats updates</td>
    <td>Leader board stats updates</td>
    <td>Confirmed</td>
    </tr>
</tbody>
</table>

## Credits:

- [Printing on same line python](https://www.tutorialspoint.com/how-to-print-in-same-line-in-python)
- [Hacked Password List](https://parade.com/living/most-common-passwords)
- [Wordle](https://www.nytimes.com/games/wordle/index.html) - Main inspiration for the game

## Notes:
- Commit messages: usually feat add style add etc.. is added as a preface to the commit messages, but since it is only python style add etc.. did not make sense to preface every commit with "Pyhon" for an entirely python project.
- Wildcard imports as the functions are bespoke built by me I used a wildcard import "*" to import the modules, if this wasn't the case I would import selected modules only / functions only

## Deployment:
This application is deployed on Heroku using the below instructions

1. Login to heroku
2. Create a new app
   
   ![Create new app Heroku](assets/documentation/heroku_new_app.jpg)
   
3.Complete App Name form

   ![Heroku App Name form](assets/documentation/heroku_app_name.jpg)
   
4. Deploy using github

   ![Heroku Github connected](assets/documentation/heroku_deploy_github.jpg)
   
5. Connected to main brach (this was connected to a testing branch for testing purposes)
   
   ![Heroku connected to Github main Branch](assets/documentation/heroku_deployment_main_branch.jpg)
   
7. Added CREDS to the Config Vars (the value is hidden intentionally)
   
   ![creds config vars Heroku](assets/documentation/creds_config_vars.jpg)
   
8. Set port to 8000 as required for the terminal to run correctly
   
   ![Port config vars heroku](assets/documentation/port_config_vars.jpg)

9. Enable automatic deployments from Branch Main
10. Deploy Manually

## Bugs
### Unfixed
- When resizing the terminal screen the text vanishes from the terminal, this is from the Template used and is not due to my code

No other bugs noted during testing

