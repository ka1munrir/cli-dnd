import inquirer, os
from models.players import Players
from models.characters import Characters
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
    questions = [
        inquirer.List('option',
                      choices = ["thing 2", "thing 1", "Create New Character", "Log Out"],
                      ),
    ]
    answer = inquirer.prompt(questions)
    if answer["option"] == "Create New Character":
        character_creation(player)
    elif answer["option"] == "Log Out":
        exit()


def character_creation(player):
    clear()
    questions = [
        inquirer.Text('name', message = "Name"),
        inquirer.List('race',
                      message = "Race",
                      choices = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "half-orc", "halfling", "human", "tiefling"],
                      ),
        inquirer.List('class',
                      message = "Class",
                      choices = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"],
                      ),
                    #   level is just 1
        inquirer.Text('background', message = "Background"),
                    #   proficiency is 2 + floor(level - 1/4)
        inquirer.Text('passive_perception', message = "Passive Perception"),
        inquirer.Text('armor_class', message = "Armor Class"),
        inquirer.Text('speed', message = "Speed"),
        inquirer.Text('hp', message = "Hit Points"),
                    #   temp hp is 0
        inquirer.Text('hit_dice', message = "Hit Dice Value"),
    ]
    answer = inquirer.prompt(questions)
    # print(answer["passive_perception"])
    Characters(player[0], answer["name"], answer["race"], answer["class"], 1, answer["background"], 2, int(answer["passive_perception"]), int(answer["armor_class"]), int(answer["speed"]), int(answer["hp"]), 0, int(answer["hit_dice"]))


def exit_program():
    print("Goodbye!")
    exit()

