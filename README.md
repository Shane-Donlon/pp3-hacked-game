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
