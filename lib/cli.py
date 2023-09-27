from helpers import *
from asciiArt import character_creator
import inquirer, os

def main():
    os.system("clear")
    print(character_creator)
    questions = [
        inquirer.List('option', 
                      message = "Welcome to your CLI DnD Character Creator",
                      choices = ["Log in", "Sign up", "Exit"],
                      ),
    ]
    answer = inquirer.prompt(questions)
    if answer["option"] == "Exit":
        os.system('clear')
        exit_program()
    elif answer["option"] == "Sign up":
        os.system('clear')
        sign_up()
    elif answer["option"] == "Log in":
        os.system("clear")
        log_in()
    else:
        print(answer)
    


if __name__ == "__main__":
    main()