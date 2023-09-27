import inquirer, os, time
from models.players import Players
from models.characters import Characters
from asciiArt import *

def clear():
    os.system("clear")

def main():
    clear()
    print(character_creator)
    questions = [
        inquirer.List('option', 
                      message = "Welcome to your CLI DnD Character Creator",
                      choices = ["Log in", "Sign up", "Exit"],
                      ),
    ]
    answer = inquirer.prompt(questions)
    if answer["option"] == "Exit":
        clear()
        exit_program()
    elif answer["option"] == "Sign up":
        clear()
        sign_up()
    elif answer["option"] == "Log in":
        clear()
        log_in()

def sign_up():
    questions = [
        inquirer.Text('username', message = "Username"),
        inquirer.Text('password', message = "Password"),
    ]
    answers = inquirer.prompt(questions)
    try:
        Players(answers["username"], answers["password"])
        main()
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
    character_list = [character for character in Characters.get_by_user(player[0])]
    home_choices = [character[2] for character in character_list]
    home_choices.extend(["Create New Character", "Delete Character", "Log Out"])

    print(player_home)
    questions = [
        inquirer.List('option',
                      choices = home_choices,
                      ),
    ]
    answer = inquirer.prompt(questions)
    if answer["option"] == "Create New Character":
        character_creation(player)
    elif answer["option"] == "Delete Character":
        character_deletion(player, character_list)
    elif answer["option"] == "Log Out":
        main()
    else:
        pass


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

    print(f'Creating {answer["name"]}...')
    time.sleep(2)
    home(player)

def character_deletion(player, character_list):
    questions = [
        inquirer.List('option',
                      message = "Which character do you want to delete",
                      choices = [character[2] for character in character_list],
                      ),
    ]
    answer = inquirer.prompt(questions)
    char_to_del = 0
    for character in character_list:
        if character[2] == answer["option"]:
            char_to_del = character[0]
    Characters.delete(char_to_del)
    print(f"\n\n{answer['option']} has been deleted")
    time.sleep(2)
    home(player)

def exit_program():
    print("Goodbye!")

