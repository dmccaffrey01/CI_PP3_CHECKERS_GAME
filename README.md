# Checkers Game
(Developer Dillon Mc Caffrey)

![Site Image](docs/site-image.png)

[Live Site](https://ci-pp3-checkers-game.herokuapp.com/) is hosted on Heroku

## About

This is a command-line version of the classic Checkers for one, two or even zero players.

Checkers is a classic board game that is played on an 8x8 board with 64 squares of alternating
colors, red and yellow in this game. The game is played between two players, who each have
12 pieces in their respective colors, either white or black, arranged on opposite sides of the
board.

The objective of the game is to capture all of the opponent's pieces or to block them so they
cannot make any more moves.

The rules of checkers are as follows:

Players take turns moving one piece diagonally forward on the dark squares.

Normal pieces can only move forward, but if they reach the last row on the opposite side of the 
board, they can be promoted to a king, which can move diagonally in any direction.

Captures are made by jumping over an opponent's piece that is adjacent and landing on an
empty square. Multiple jumps are allowed in one turn.

If there is a choice between multiple captures, the player can choose which one to make.

The game ends when one player captures all of the opponent's pieces or blocks them so they cannot
make any more moves.

If a player is unable to make a move or has no legal moves left, they lose the game.

These are the basic rules of checkers, but there are variations in rules depending on the
location and culture where it is played.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Site User](#site-user)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
- Play a game of checkers against other players
- Play a game of checkers against the computer
- Have their stats recoreded
- Have a fun time

### Site Owner Goals
- Create a fun checkers game
- Create a game that the user can easily understand how to play
- Allow the user to have a great user experience when playing the game
- Give the user options in all areas of the program

## User Experience

### Target Audience
- People who play board games like chess and checkers
- People who want to play against their friends
- People who want to play against the computer

### User Requirements and Expectations
- Functioning game mechanics and experience
- A way to log in and record a players stats
- Test game features
- View how to play the game
- Get in contact with the developer

### User Manual
<details>
<summary>Click here to view instructions</summary>

#### Main Menu
When the program is run the user is presented with the main menu, the main menu consists of ASCII art presenting "Checkers", and options to choose from
The user is asked to input the option they would like to choose and press enter key
These are the options
1. Play Game
2. View Game rules
3. View Leaderboard
4. Test Features
5. Exit Game

If the user inputs incorrect option the user is asked to try again and is prompted to enter input.
This happens throughout the entire program when user is asked for input
At any point in the logging in process the user can enter "r" to return to the main menu.

#### Play Game
When the Play Game option is selected, the user is asked to enter more input.
The user is asked "How many players?" with 3 options to choose from:
1. One (Player vs CPU)
2. Two (Player vs Players)
3. None (CPU vs CPU)

#### One (Player vs CPU)
When the user selects one, another question is asked.
The user is asked "Has player 1 played before and have an existing accout?" with 2 options to choose from:
1. Yes
2. No

#### Log In Name
When the user chooses Yes, the user is asked "Enter name of player 1".
The user is prompted to enter their name as input.

#### Log In Email
When the user enters their name they are then asked to "Enter email of 'name entered'".
The user is prompted to enter their email as input.

#### Level of difficulty of CPU and Entered Valid Email and Registered
The program checks first if the email is valid by having an @ sign and a domain like .com. 
If it is valid it then checks if the email is registered. If it is registered Logging in is printed
and a new question is asked: "What level of difficulty whould you like the cpu to be?"
Three options are presented: 
1. Beginner
2. Novice
3. Expert
The user is prompted to input one of these options and then the game starts

#### Invalid Email Inputed
If the email entered isn't valid meaning it doesn't have an @ or domain, the user is displayed with an error message and asked to input the email again until it is a valid email

#### Email Not Registered
If the user enters a valid email but that email is not registered yet, the user is displayed with email address not found on database and asked another question. "What would you like to do" and the user is given 2 options:
1. Try entering email again
2. Register as new player
If the user selects option 1 they are brought back to entering a email that is valid and regiserted.
If the user selects option 2 they are displayed with registering alert and then presented with choosing the level of difficulty of CPU and their email is now registered to the system

#### Register Name
When the user selects option 2 "No" for has the player played before or have a registered account. The program asks the user to enter their name similar to log in.
The user is prompted to enter their name.

#### Register Email
After the user hase entered their name they are then prompted to enter their email.
The same as logging in the email is verified to have an @ and a domain and asks the user to reenter email if invalid. The program then checks if the entered email has not been registered

#### Entered Registered Email
If the email entered is already registered an error alert is displayed and then the user is asked to choose from 2 options:
1. Try entering email again
2. Sign in as that player
If the user selects option 1, they are brought back to entering email that is valid and not registered in system.
If the user selects option 2, they are brought to the CPU difficulty selection and they are logged in as the entered email.

#### Two (Player vs Player)
If the user selects option 2 when selecting how many players, the user is brought through the same process as selection option 1 but for 2 players. Player 1 enters if they have played then either logs in or registered but this time instead of selecting CPU difficulty the user logs or registers player 2. And once both players are logged in or registered the game starts

#### None (CPU vs CPU)
If the user selects option 3 when selecting how many players, the user skips over logging or registering any players and goes straight to selecting CPU difficulty. This time the user selects CPU difficulty for 2 CPUs.
First being black and the next being white.

#### Start Game
When one, both or neither players have logged in, selected CPU difficulty and the game starts the board is displayed.
White pieces are at the top and black are at the bottom. Player 1(or CPU 1) is black and player 2 (or CPU 2) is white. Black moves first in checkers.

#### Select Piece
When the game starts and board is displayed.
The user is asked to choose a piece from the movable pieces of their color.
They are presented with however many options depending on the amount of movable pieces.
Options are numbered 1 to however many and ordered from pieces higher up on the board.
If their is a CPU playing this does not happen.

#### Select Move
Once the player has selected a piece the user is then asked to choose a move from the available moves of that piece.
They are presented with however many options depending on the amount of available moves for that piece.
Options are numbered 1 to however many and orded jumps first, then normal moves from left to right then kings moves from left to right.
If their is a CPU playing this does not happen. The CPU selects a move based on a algorithm

#### CPU Select move
Depending on the difficulty of the CPU the CPU selects a move based on a algorithm. If CPU is Beginner the CPU selects a random move from all available moves. If the CPU difficulty is Novice, the CPU selects a move based on a min max algorithm that looks all moves 2 moves in advance. And if the CPU difficulty is Expert, the CPU selects a move based on a min max algorithm that looks at all moves 4 moves in advance

#### Move piece
Once the player has selected a move the piece is then moved to the position selected and any pieces that were jumped are removed. It is then the next persons go. If there are 2 players, player 2 goes through the same process of selecting pieces, and moves but just for the opposite color. The CPU goes through its same process depending on difficulty.

#### Game Over
Once a game has progressed and if one player or CPU, cannot move another piece, either from not having any pieces or their pieces are blocked. The program displays game over and prints out the winner.
Game stats are then shown, where it shows the updated games, wins and loses and total moves of the game.

#### After Game Selection
After the game over has been displayed, the user is then asked what to do next. They have 4 options:
1. Play again
2. Return to main menu
3. View the leaderboards
4. Quit
Option 1 starts a new game with the same players.
Option 2 returns the user to the main menu 
Option 3 brings the user to view the leaderboards and then return to the main menu
Option 4 exits the programme

#### View Game Rules
When the user selects view game rules in the main menu, they are displayed with information on how to play the game and the rules to follow.
They are then prompted to enter option 1 the only option to return back to the main menu

#### View Leaderboard
When the user selects view leaderboard in the main menu, they are displayed with a table showing all the players regiserted in the system ranked in order. The defaul rank order is by wins where most wins is the player ranked number 1.
The user is displayed with 4 options to choose from. These options sort the ranks or returns to main menu.
1. Wins
2. Total Games
3. Loses
4. Return to main menu
Option 1 sorts ranks by most wins
Option 2 sorts ranks by total games played
Option 3 sorts ranks by least loses
Option 4 returns the user to the main menu

#### Test Features
When the user selects test features in the main menu, they are displayed with 6 options to choose from.
These options are:
1. Single Jump
2. Double Jump
3. Triple Jump
4. Quintuple Jump
5. King
6. Jump to King
Any of these options set up a board to test the feature selected.
The program creates a new board and starts a game where the user can test these features

#### Exit Game
When the user selects exit game in the main menu, the program displays a goodbye message and exits the programme.
</details>

## User Stories

### Site User

1. I want a nice and easily navigated main menu
2. I want to be able to choose to play against the computer or player, or have 2 computers play against eachother
3. I want to be able to log in to the game
4. I want to be able to register if I have never played before
5. I want to personalise the game by entering my name
6. I want to change the level of difficulty of the computer
7. I want the board to be displayed in a nice and easy to understand way
8. I want to have options like replay the game, or return to the main menu after I have finished the game
9. I want to view the game rules and receive information on how to play
10. I want my stats to be displayed in a leaderboard
11. I want to sort the leaderboard in different ways
12. I want to be able to test certain game features
13. I want to be able to easily exit the programme from the main menu

### Site Owner

14. I want the user to enter valid emails when registering or logging in
15. I want to store the user data so I can use it in the programme
16. I want the user to receive feedback if they enter invalid input
17. I want to thank the user for playing the game
18. I want the user to choose to register a new email or try entering email again if they are logging in and enter email that isn't on system
19. I want the user to choose to log in as entered email or try entering email again if they are registering a new email that is already on system
20. I want the user to be able to return to the main menu when they are logging in or registering
21. I want the user to be able to select a piece to move from their movable pieces on the board
22. I want the user to be able to select a move from the available moves of the piece they selected

## Technical Design

### Flowchart

The following flowchart summarises the structure and logic of the application.

<details><summary>Flowchart</summary>
<img src="docs/flowchart.png">
</details>

### Languages

- [Python](https://www.python.org/) was used for the programming of logic of the app
- [Node.js](https://www.nodejs.org/) was also used in the deployment of the app

### Frameworks & Tool
- [Font Awesome](https://fontawesome.com/) - icons from Font Awesome were used in the footer below the program terminal
- [Drawio](https://github.com/jgraph/drawio-desktop/releases/tag/v20.8.16) was used to draw a program flowchart
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Cloud Platform](https://cloud.google.com/cloud-console/) was used to manage access and permissions to the Google Services such as Google auth, sheets etc.
- [Google Sheets](https://www.google.co.uk/sheets/about/) were used to store players details
- [PEP8 Code Institute Linter](https://pep8ci.herokuapp.com/) was used to check my code against Python conventions
- [GitPod](https://gitpod.io) was used as workspace to edit code
- [Heroku](https://heroku.com) was used to host the website

### Libraries

#### Python Libraries
- os
- sys
- time
- math
- random
- itemgetter
- io
- [unittest](https://docs.python.org/3/library/unittest.html) - used to carry out testing

#### Third Party Libraries
- [colorama](https://pypi.org/project/colorama/) - I used this library to add color to the terminal and enhance user experience.
- [email_validator](https://pypi.org/project/email-validator/) - I used this library to validate the user email to check if the email exists
- [gspread](https://docs.gspread.org/en/latest/) - I used gspread to add and change data in my Google spreadsheet and to interact with Google APIs
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - I used this module to set up the authentication required for accessing the Google API and connecting my Service Account with the Credentials function. I created a creds.json file containing all the necessary details for the API to access my Google account.

## Features

### Validate Input
- Throughout the entire program there are functions that validate the input entered to make sure the input is an option
- Every choice the user has the input is validated and if the user enters invalid input the user is asked to input correct valid input

![Invalid Input](docs/invalid-name-feature.png)

### Main Menu
- Provides the user with a welcome screen where they can easily navigate through the program
- Acts as a hub where the user returns to multiple times when using the program
- User Stories covered: 1

![Main Menu](docs/main-menu-feature.png)

### Return To Main Menu
- If the user enters "r" at any point when they are registering, they will be returned back to the main menu
- User Stories Covered: 20

![Return to Main Menu](docs/return-to-menu-feature.png)

### Choose Number of Players
- Allows the user to choose how many players are going to play
- Add a unique experience to whatever you choose
- Add variety to the game
- User Stories covered: 2

![Choose Number of Players](docs/num-players-feature.png)

### Log In or Register
- Allows the user to log in or register, so they can record their stats and rank higher on the leaderboard
- Personalises the game as the game can now display your name and stats
- Asks if user is registered, then their name, and email and then logs in or registers them
- User Stories covered: 3, 4, 5, 15

![Log In or Register](docs/login-register-feature.png)

### Ask Registered
- Asks if user if they have played before, this allows them either to log in or register a new account
- If answered yes they log in
- If answered no they register a new account

![Ask Registered](docs/login-register-feature.png)

### Ask Name
- Asks the user to input their name
- Name has to be valid, meaning it has to be in the alpha(a-z, A-Z) characters no numbers and of length (1-12) no longer
- An error message is displayed to user if not valid and asked to type again

![Invalid Name](docs/invalid-name-feature.png)

### Ask Email
- Asks the user to input their email
- Email has to be valid, meaning it has to be in the form of valid email eg(name@gmail.com)
- An erro message is displayed to user if not valid and asked to type again

![Invalid Email](docs/invalid-email-feature.png)

### Validate Email 
- Checks if the email is valid and is registered
- Displays error alert if the user typed in invalid input or the email was not registered
- User Stories covered: 14, 16

![Log In or Register](docs/login-register-feature.png)

### Email Not Registered
- If the user inputs that they have played and tries to log in instead of register but they type in an email that hasn't been registered an error message appears (eg. invalid@gmail.com)
- The user is then asked if they would like to register a new account, where they will register the email inputed and there email will be added to the systeem
- The other option is to retype the email where they will be asked to input email again and the same proccess of validation will occur
- User Stories Covered: 18

![Email Not Registered](docs/email-not-registered-feature.png)

### Email Already Registered
- If the users inputs that they have not played and tries to register an account that is already in the system an error message appears (eg. dil@gmail.com)
- The user is asked if they would like to log in as that player or register a new email
- If they choose to log in it logs them in as that email, if they choose to register new email they will be asked to input email again and the same process of validation will occur
- User Stories Covered: 19

![Email Already Registered](docs/email-already-registered-feature.png)

### CPU Diffiuclty
- Allows the user to choose what level of difficulty they want the game to be
- This adds variety and changes up the gameplay
- It also makes it interesting to learn from as the computer calculates moves in advance
- User Stories covered: 6

![CPU Difficulty](docs/cpu-difficulty-feature.png)

### Start Game
- When the user has logged in successfully, the game starts
- The board is displayed to the user and then the user can select a piece to move
- User Stories Covered: 7

![Start Game](docs/start-game-feature.png)

### Select Piece
- Allows the user to select what piece they would like to move from movable pieces
- Displays the options the user has to choose from
- User can input what piece to select
- User Stories Covered: 21

![Select Piece](docs/select-piece-feature.png)

### Select Move
- Allows the user to select what move they would like from available moves
- Displays the options the user has to choose from when they select a piece
- Allows the user to return from selecting a move to select a new piece by entering "r"
- User Stories Covered: 22

![Select Move](docs/select-move-feature.png)

### Game Over
- Displays a game over message when the game is finished
- Congratulates the winner of the game

![Game Over](docs/game-over-feature.png)

### After Game Selection
- Displays game stats and updates both players stats for leaderboard
- Allows the user to select what to do next, if they want to play again, return to leaderboard or view leaderboard or quit game
- User Stories Covered: 8

![After Game Selection](docs/after-game-feature.png)

### View Game Rules
- Displays to the user information on how to play the game and what the rules of the game are
- Allows the user to return to main menu again
- User Stories Covered: 9

![View Game Rules](docs/game-rules-feature.png)

### View Leaderboard
- Displays all users that have registered in a table, ranking them on a particular stat
- Allows the user to check their wins, loses, and total games played
- User Stories covered: 10

![View Leaderboard](docs/leaderboard-feature.png)

### Sort Leaderboard Ranks
- Allows the user to choose how to sort the ranks of the leaderboard
- They can sort it by wins, loses or total games
- User Stories covered: 11

![Sort Leaderboard Ranks](docs/leaderboard-feature.png)

### Test Features
- Allows the user to set up certain game states in order for user to test a certain functionality or feature of the game
- The user can choose from 6 features to test
- This creates a test game where a test board is set up
- User Stories covered: 12

![Test Features](docs/test-feature-feature.png)

### Exit Game
- Allows the user to exit the application
- Displays a thank you message for the user then it exits the application
- User Stories covered: 13, 17

![Exit Game](docs/exit-feature.png)

## Validation

[CI PEP8 Validation Service](https://pep8ci.herokuapp.com/#) was used to check the code for PEP8 requirements. All the code passes with no errors and 1 warning across all files
The 1 warning is "E402 module level import not at top of file", this is because I used sys.path to access files in folders. I know how to get rid of this warning, and I will explain in Bugs but I would prefer not to.

<details>
<summary>Validation for run.py</summary>
<img src="docs/run-validation.png">
</details>

<details>
<summary>Validation for display.py</summary>
<img src="docs/display-validation.png">
</details>

<details>
<summary>Validation for game_rules.py</summary>
<img src="docs/game-rules-validation.png">
</details>

<details>
<summary>Validation for leaderboard.py</summary>
<img src="docs/leaderboard-validation.png">
</details>

<details>
<summary>Validation for main_menu.py</summary>
<img src="docs/main-menu-validation.png">
</details>

<details>
<summary>Validation for checkers_engine.py</summary>
<img src="docs/checkers-engine-validation.png">
</details>

<details>
<summary>Validation for checkers.py</summary>
<img src="docs/checkers-validation.png">
</details>

<details>
<summary>Validation for feature_testing.py</summary>
<img src="docs/ft-validation.png">
</details>

<details>
<summary>Validation for smart_move_finder.py</summary>
<img src="docs/smf-validation.png">
</details>

<details>
<summary>Validation for test_checkers_engine.py</summary>
<img src="docs/test-check-eng-validation.png">
</details>

<details>
<summary>Validation for test_checkers.py</summary>
<img src="docs/test-check-validation.png">
</details>

<details>
<summary>Validation for test_display.py</summary>
<img src="docs/test-display-validation.png">
</details>

<details>
<summary>Validation for test_feature_testing.py</summary>
<img src="docs/test-ft-validation.png">
</details>

<details>
<summary>Validation for test_game_rules.py</summary>
<img src="docs/test-gr-validation.png">
</details>

<details>
<summary>Validation for test_leaderboard.py</summary>
<img src="docs/test-leaderboard-validation.png">
</details>

<details>
<summary>Validation for test_main_menu.py</summary>
<img src="docs/test-main-menu-validation.png">
</details>

<details>
<summary>Validation for test_smart_move_finder.py</summary>
<img src="docs/test-smf-validation.png">
</details>

## Testing

I first manually tested the user storeis
Then I set up automated unit testing using the python unittest library and checked coverage on it to see what tests I was covering

### Manual Testing
<details>
<summary>See testing of user stories</summary>

1. I want a nice and easily navigated main menu

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main menu | Start App | Users are presented with main menu | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-feature.png">
</details>

2. I want to be able to choose to play against the computer

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Choose Number of Players | Selection option 1 | Users are presented with option to choose the number of players and play against the computer | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
</details>

3. I want to be able to log in to the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Log In or Register | Selection option 1, then option 1 or 2 | Users are presented with option to choose to log in or register, they can enter their name and email | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
</details>

4. I want to ber able to register if I have never played before

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Log In or Register | Selection option 1, then option 1 or 2 | Users are presented with option to choose to log in or register, they can enter their name and email | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
</details>

5. I want to personalise the game by entering my name

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Log In or Register | Selection option 1, then option 1 or 2 | Users are presented with option to choose to log in or register, they can enter their name and email | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
</details>

6. I want to change the level of difficulty of the computer

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| CPU Difficulty | Selection option 1, then option 1 or 2, Enter in log in details | Users are presented with option to choose to the level of difficulty of Computer with 3 options | Works as expected |
| CPU Difficulty | Selection option 1, then option 3 | Users are presented with option to choose to the level of difficulty of Computer with 3 options | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
<img src="docs/cpu-difficulty-test.png">
</details>

7. I want the board to be displayed in a nice and easy to understand way

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Start Game | Selection option 1, then option 1 or 2, Enter in log in details | Users are presented with game board and their pieces | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
<img src="docs/cpu-difficulty-test.png">
<img src="docs/start-game-feature.png">
</details>

8. I want to have options like replay the game, or return to the main menu after I have finished the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| After Game Selection | Selection option 1, then option 1 or 2, Enter in log in details, play game of checkers | Users are presented with option to play game, return to main menu, view leaderboard or exit app | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
<img src="docs/cpu-difficulty-test.png">
<img src="docs/start-game-feature.png">
<img src="docs/select-move-test.png">
<img src="docs/select-piece-test.png">
<img src="docs/after-game-selection.png">
</details>

9. I want to view the game rules and receive information on how to play

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| View Game Rules | Select option 2 | Users are presented with game rules and option to return to main menu | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-2-test.png">
</details>

10. I want my stats to be displayed in a leaderboard

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| View Leaderboard | Select option 3 | Users are presented with leaderboard of all players registered | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-3-test.png">
</details>

11. I want to sort the leaderboard in different ways

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| View Leaderboard | Select option 3 | Users are presented with leaderboard of all players registered and the option to sort the ranks depending on option selected | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-3-test.png">
<img src="docs/leaderboard-test.png">
</details>

12. I want to be able to test certain game features

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Test Features | Select option 4 | Users are presented with options to choose a test scenario to test game features | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-4-test.png">
<img src="docs/test-feature-test.png">
</details>

13. I want to be able to easily exit the programme from the main menu

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Exit Game | Select option 5 | Users are presented with goodbye message and app exits | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-5-test.png">
</details>

14. I want the user to enter valid emails when registering or logging in

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Validate Email | Select option 1, Select option 1 or 2, Enter name then email | Users are presented with loggin in message or error message if email invalid | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/login-register-test.png">
</details>

15. I want to store the user data so I can use it in the programme

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Log In or Register | Select option 1, Select option 1 or 2, Enter name then email | Users are presented with loggin in message or error message if email invalid, Name and stats are then recorded and displayed | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
</details>

16. I want the user to receive feedback if they enter invalid input

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Validate Email | Select option 1, Select option 1 or 2, Enter name then email | Users are presented with loggin in message or error message if email invalid | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/login-register-test.png">
</details>

17. I want to thank the user for playing the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Exit Game | Select option 5 | Users are presented with goodbye message and app exits | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-5-test.png">
</details>

18. I want the user to choose to register a new email or try entering email again if they are logging in and enter email that isn't on system

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Email Not Registered | Select option 1, select option 1 or 2, select option 1 to log in, enter a name, then enter an email that isn't registered | Users are presented with an error message then asked to choose to try entering email again or register the email entered into the system | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/email-not-registered-test.png">
</details>

19. I want the user to choose to log in as entered email or try entering email again if they are registering a new email that is already on system

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Email Already Registered | Select option 1, select option 1 or 2, select option 2 to register, enter a name, then enter an email that is already registered(eg. dil@gmail.com) | Users are presented with an error message then asked to choose to try entering a new email or log in as the email entered  | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/email-already-registered-test.png">
</details>

20. I want the user to be able to return to the main menu when they are logging in or registering

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Return To Main Menu | Select option 1, select option 1 or 2, enter r to return to main menu | Users are presented with a message that they are returning to the main menu | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/return-to-main-menu-feature.png">
</details>

21. I want the user to be able to select a piece to move from their movable pieces on the board

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Select Piece | Select option 1, select option 1 or 2, select option 1 or 2 to register or log in, register or log in by entering name and email, select option to choose a piece to move | Users are presented with options to choose piece | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/return-to-main-menu-feature.png">
<img src="docs/login-register-test.png">
<img src="docs/select-piece-feature.png">
</details>

22. I want the user to be able to select a move from the available moves of the piece they selected

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Select Move | Select option 1, select option 1 or 2, select option 1 or 2 to register or log in, register or log in by entering name and email, select option to choose a piece to move, select a move you want the piece to move to | Users are presented with options to choose piece and then options to choose a move | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/main-menu-option-1-test.png">
<img src="docs/num-players-test.png">
<img src="docs/return-to-menu-feature.png">
<img src="docs/login-register-test.png">
<img src="docs/select-piece-feature.png">
<img src="docs/select-move-feature.png">
</details>

</details>

### Automated Unit Testing

<details><summary>See unit testing</summary>

- I wrote unit tests for all python files using the unittest library
- All unit test files are in the folder test
- I used mock functions and classes to help out and run all tests
- I then used coverage library to run the tests and check how much of my code was being tested
- When you coverage run, there is a total of 161 tests
- I achieved 99% report, the 1% is the test files but all other files are 100%, meaning my code is 100% tested

<details><summary>See coverage details</summary>
<img src="docs/unittests.png">
<img src="docs/coverage-run-report.png">
</details>

## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| When passing code through the pep8 Linter, a "E402 module level import not at top of file" warning comes up | This is caused because I am importing a file from a different folder, I am using sys.path to get the path and redirect it to the folder. To fix this I need to create a setup.py file and install my files into the app, but I would prefer not to do this and instead have them imported the way I do. I could also use ".." and "from" when importing but this caused an error when importing in unit testing so I would also prefer not to do that.
| When playing the game, if the player has a lot of options either from pieces or moves, the output of choosing the option can cause the terminal to scroll down. Sometimes when the terminal scrolls down and when you scroll back up the board can become messed up and stay at the top. | This doesn't happen often but a fix could be to reduce the size of the board or alternitavely have the options of pieces to move be displayed on the same line instead of one below another. |

</details>

## Deployment
This application has been deployed from GitHub to Heroku. A guide to deploying to Heroku can be found [here](https://devcenter.heroku.com/articles/github-integration)
Here are the steps to deployment
- Login or create an account at [Heroku](https://dashboard.heroku.com/)

<img src="docs/deployment-1.png">

- Click on New > Create new app in the top right of the screen.

<img src="docs/deployment-2.png">

- Add an app name and select location, then click 'create app'.

<img src="docs/deployment-3.png">

- Under the deploy tab of the next page, select connect to GitHub.

- Log in to your GitHub account when prompted.

<img src="docs/deployment-4.png">

- Select the repository that you want to be connected to the Heroku app.

<img src="docs/deployment-5.png">

- Click on the settings tab.

<img src="docs/deployment-6.png">

- Scroll down to the config vars section, and add 2 config vars:
    * The first key is CREDS and the value here is the creds.json file that was generated for the google sheets API to work properly.
    * The second key is PORT and the Value is 8000
  

<img src="docs/deployment-7.png">

- Once you have set up the config vars, scroll down to buildpacks (still under the settings tab)

- Add the Python and Node.js buildpacks to your app and make sure that when they are displayed, they appear in the order:
    * Python
    * Node.JS
  

<img src="docs/deployment-8.png">

- Navigate back to the settings tab.

- Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.

<img src="docs/deployment-9.png">

- In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.

<img src="docs/deployment-10.png">


### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits

- [Code Institue](https://learn.codeinstitute.net/dashboard) Love Sandwiches Walkthrough for the google spreadsheet API and credentials
- [Stackoverflow](https://stackoverflow.com/) for help with python bugs
- [Eddie Sharick](https://www.youtube.com/@eddiesharick6649) for help on AI smart move algorithm

## Acknowledgements

I would like to thank and acknowledge the following people who helped me along the way in completting this project:

Code Institute - for giving me guideance and support throughout the project

Mo Shami - for being the mentor to guide me through the project and give essential feedback

Amy Connolly - for peer reviewing and giving feedback on the website

Gary Mc Caffrey - for peer reviewing and giving feedback on the project






