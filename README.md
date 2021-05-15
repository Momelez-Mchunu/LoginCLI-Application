# LoginCLI-Application
LoginCLI-Application is a command line application that allows the user to sign up, login or exit 

The application is implemented using Python and SQLite3

These commands are executed using a specific number that corresponds to that command

0 -exiting the program

1 -loging in to the system,provided your username and password are on the database

2- Signing up, if you are new to the system you have to sign up

with the *0* command:
   * The program exits

With the *1* command:
* The program asks for the username, if username is empty, the program exits.
* if username is not empty, it asks for the password if username and password exist on database user is logged
* if password is incorrect, the program prompts the user for the username.
* if non-existent/incorrect details are entered 3 times the program exits.

With the *2* command:
* The program asks the user for a username, if username is empty the program exits
* if username already exists, the user is prompted to enter another username
* the user is then prompted for a password, if password is empty the user is given another chance to enter a password
* if password is empty again, the program then exist.

Libraries used
SQLite3
* used for connecting the database and executing SQL statement
GetPass
* used for masking the masking the password as the user enters it.
 


