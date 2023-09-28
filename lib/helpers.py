import inquirer, os, time, random, math
from models.players import Players
from models.characters import Characters
from models.charAttributes import CharAttributes
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
        char_to_disp = None
        for character in character_list:
            if character[2] == answer["option"]:
                char_to_disp = character
        display_character(player, char_to_disp)

def display_character(player, character):
    clear()
    print(f"Name: {character[2]}")
    print(f"Race: {character[3]}")
    print(f"Background: {character[6]}")
    print(f"Level {character[5]} {character[4].capitalize()}")
    questions = [
        inquirer.List('option',
                      choices = ["Attributes", "Skills", "Spells", "Items", "Level Up", "Back"],
                      ),
    ]
    answer = inquirer.prompt(questions)
    if answer["option"] == "Attributes":
        attribute_display(player, character)
    elif answer["option"] == "Skills":
        pass
    elif answer["option"] == "Spells":
        pass
    elif answer["option"] == "Items":
        pass
    elif answer["option"] == "Level Up":
        Characters.level_up(character[0])
        time.sleep(1)
        display_character(player, Characters.get_by_id(character[0]))
    elif answer["option"] == "Back":
        home(player)

def attribute_display(player, character):
    clear()
    attr = CharAttributes.get_by_char(character[0])
    print(f"{character[2]}'s Attributes")
    print(f"STR: {attr[2]}   {math.floor((attr[2] - 10)/2)}")
    print(f"DEX: {attr[3]}   {math.floor((attr[3] - 10)/2)}")
    print(f"CON: {attr[4]}   {math.floor((attr[4] - 10)/2)}")
    print(f"INT: {attr[5]}   {math.floor((attr[5] - 10)/2)}")
    print(f"WIS: {attr[6]}   {math.floor((attr[6] - 10)/2)}")
    print(f"CHA: {attr[7]}   {math.floor((attr[7] - 10)/2)}")
    questions = [
        inquirer.List('option',
                      choices = ["Back"],
                      ),
    ]
    answer = inquirer.prompt(questions)
    if answer["option"] == "Back":
        home(player)


def character_creation(player):
    clear()
    name = input("Name: ")
    player_characters = [character[2] for character in Characters.get_by_user(player[0])]
    if name in player_characters:
        print (f"You already have a character called {name}. Please rename your new character")
        time.sleep(2)
        character_creation(player)
    else:

        questions = [
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
                        #   proficiency is 2 + floor(level - 1/4),
            inquirer.Text('armor_class', message = "Armor Class"),
            inquirer.Text('speed', message = "Speed"),
            inquirer.Text('hp', message = "Hit Points"),
                        #   temp hp is 0
            inquirer.Text('hit_dice', message = "Hit Dice Value"),
        ]
        answer = inquirer.prompt(questions)
        attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        priority = [1, 2, 3, 4, 5, 6]
        priority_list = []
        for attribute in attributes:
            questions2 = [
                inquirer.List(
                    f'{attribute}',
                    message = f"Please rank the priority of {attribute} from 1-6 (high-low):",
                    choices = priority
                )
            ]
            att_priority = inquirer.prompt(questions2)
            priority_list.append(att_priority)
            priority.remove(att_priority[f'{attribute}'])

        priority_list = [list(dic.values())[0] for dic in priority_list]
        # print(type(priority_list[0]['Strength']))
        attribute_rolls = []
        for attribute in attributes:
            d64x = [random.randint(1,6) for i in range(4)]
            d64x.sort()
            d64x.pop(0)
            attribute_rolls.append(sum(d64x))
        attribute_rolls.sort(reverse = True)
        attribute_vals = priority_list.copy()
        
        for i in range(5):
            for j in range(5):
                if priority_list[j] == i + 1:
                    attribute_vals[j] = attribute_rolls[0]
                    attribute_rolls.pop(0)
        print(attribute_vals)
        Characters(player[0], name , answer["race"], answer["class"], 1, answer["background"], 2, int(answer["armor_class"]), int(answer["speed"]), int(answer["hp"]), 0, int(answer["hit_dice"]))
        new_char = Characters.get_by_user_and_name(player[0], name)
        CharAttributes(new_char[0], attribute_vals[0], attribute_vals[1], attribute_vals[2], attribute_vals[3], attribute_vals[4], attribute_vals[5])
        print(f'Creating {name}...')
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

