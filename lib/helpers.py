import inquirer, os
from models.players import Players
from asciiArt import player_home

def clear():
    os.system("clear")

def sign_up():
    questions = [
        inquirer.Text('username', message = "Username"),
        inquirer.Text('password', message = "Password"),
    ]
    answers = inquirer.prompt(questions)
    try:
        return Players(answers["username"], answers["password"])
    except:
        clear()
        print("That username is already taken \n")
        sign_up()

def log_in():
    questions = [
        inquirer.Text('username', message = "Username"),
        inquirer.Text('password', message = "Password"),
    ]
    answers = inquirer.prompt(questions)
    player = Players.get_by_username(answers["username"])
    if player:
        if answers["password"] == player[2]:
            home(player)
        else:
            clear()
            print("Your password is incorrect")
            log_in()
    else:
        clear()
        print("Your username is incorrect")
        log_in()


def home(player):
    clear()
    print(player_home)
    pass


def exit_program():
    print("Goodbye!")
    exit()

