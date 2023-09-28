import inquirer, time
from charProficiencies import CharProficiencies

class Barbarian():
    hit_dice_val = 12

    @classmethod
    def start_proficencies(cls, charID):
        lightArmor = CharProficiencies(charID, 46)
        mediumArmor = CharProficiencies(charID, 56)
        shields = CharProficiencies(charID, 80)
        simpleWeapons = CharProficiencies(charID, 84)
        martialWeapons = CharProficiencies(charID, 53)
    
    @classmethod
    def skill_proficiencies(cls, charID):
        questions = [
        inquirer.Checkbox('option',
                      message = "Which skills would you like to be proficient in (Pick 2)",
                      choices = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"],
                      ),
        ]
        answer = inquirer.prompt(questions)
        if len(answer["option"]) == 2:
            pass
        elif len(answer["option"]) > 2:
            print("Only Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 2:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
    
