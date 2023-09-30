import inquirer, time
from .charProficiencies import CharProficiencies
from .proficiencies import Proficiencies
from .init import CONN, CURSOR
import sqlite3


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
        print("inside skill proficiencies")
        questions = [
        inquirer.Checkbox('option',
                      message = "Which skills would you like to be proficient in (Pick 2)",
                      choices = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"],
                      ),
        ]
        # print(charID)
        answer = inquirer.prompt(questions)
        # print(answer["option"])
        if len(answer["option"]) == 2:
            # print(charID)
            # print(answer["option"])
            sql = f'''
                    UPDATE charSkills
                    SET proficient = 1
                    WHERE character_rel = ? AND skill = ?;
                '''
            try:                
                CURSOR.execute(sql, (charID, answer["option"][0]))
                CONN.commit()
                CURSOR.execute(sql, (charID, answer["option"][1]))
                CONN.commit()
            except sqlite3.OperationalError as e:
                print(f" error: {e}")
        elif len(answer["option"]) > 2:
            print("Only Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 2:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
    
class Bard():
    hit_dice_val = 8

    @classmethod
    def start_proficencies(cls, charID):
        lightArmor = CharProficiencies(charID, 46)
        simpleWeapons = CharProficiencies(charID, 84)
        handCrossbows = CharProficiencies(charID, 34)
        longSword = CharProficiencies(charID, 49)
        rapiers = CharProficiencies(charID, 69)
        shortswords = CharProficiencies(charID, 82)

        instruments = Proficiencies.get_by_type("Musical Instruments")
        instrument_list = [instrument[1] for instrument in instruments]

        questions = [
        inquirer.Checkbox('option',
                      message = "Which instruments would you like to be proficient in (Pick 3)",
                      choices = instrument_list,
                      ),
        ]
        answer = inquirer.prompt(questions)
        if len(answer["option"]) == 3:
            for instrument in answer["option"]:
                for prof in instruments:
                    if instrument == prof[1]:
                        CharProficiencies(charID, prof[0])
                        CharProficiencies(charID, prof[1])
                        CharProficiencies(charID, prof[2])
        elif len(answer["option"]) > 3:
            print("Only Pick 3 Options!")
            time.sleep(2)
            Bard.start_proficencies(charID)
        elif len(answer["option"]) < 3:
            print("Please Pick 3 Options!")
            time.sleep(2)
            Bard.start_proficencies(charID)
    
    @classmethod
    def skill_proficiencies(cls, charID):
        questions = [
        inquirer.Checkbox('option',
                      message = "Which skills would you like to be proficient in (Pick 3)",
                      choices = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion", "religion", "sleight of hand", "stealth", "survival"],
                      ),
        ]
        answer = inquirer.prompt(questions)
        if len(answer["option"]) == 3:
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][0]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][1]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][2]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
        elif len(answer["option"]) > 3:
            print("Only Pick 3 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 3:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
    
class Cleric():
    hit_dice_val = 8

    @classmethod
    def start_proficencies(cls, charID):
        lightArmor = CharProficiencies(charID, 46)
        mediumArmor = CharProficiencies(charID, 56)
        shields = CharProficiencies(charID, 80)
        simpleWeapons = CharProficiencies(charID, 84)
    
    @classmethod
    def skill_proficiencies(cls, charID):
        questions = [
        inquirer.Checkbox('option',
                      message = "Which skills would you like to be proficient in (Pick 2)",
                      choices = ["history", "insight", "medicine", "persuasion", "religion"],
                      ),
        ]
        answer = inquirer.prompt(questions)
        if len(answer["option"]) == 2:
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][0]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][1]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
        elif len(answer["option"]) > 2:
            print("Only Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 2:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
    
class Druid():
    hit_dice_val = 8

    @classmethod
    def start_proficencies(cls, charID):
        lightArmor = CharProficiencies(charID, 46)
        mediumArmor = CharProficiencies(charID, 56)
        shields = CharProficiencies(charID, 80)
        clubs = CharProficiencies(charID, 13)
        daggers = CharProficiencies(charID, 18)
        javelins = CharProficiencies(charID, 40)
        maces = CharProficiencies(charID, 52)
        quarterstaffs = CharProficiencies(charID, 68)
        scimitars = CharProficiencies(charID, 78)
        sickles = CharProficiencies(charID, 83)
        slings = CharProficiencies(charID, 103)
        spears = CharProficiencies(charID, 105)
        herbalismKits = CharProficiencies(charID, 37)
    
    @classmethod
    def skill_proficiencies(cls, charID):
        questions = [
        inquirer.Checkbox('option',
                      message = "Which skills would you like to be proficient in (Pick 2)",
                      choices = ["arcana", "animal handling", "insight", "medicine", "nature", "perception", "religion", "survival"],
                      ),
        ]
        answer = inquirer.prompt(questions)
        if len(answer["option"]) == 2:
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][0]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][1]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
        elif len(answer["option"]) > 2:
            print("Only Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 2:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
    
class Fighter():
    hit_dice_val = 10

    @classmethod
    def start_proficencies(cls, charID):
        allArmor = CharProficiencies(charID, 2)
        shields = CharProficiencies(charID, 80)
        simpleWeapons = CharProficiencies(charID, 84)
        martialWeapons = CharProficiencies(charID, 53)
    
    @classmethod
    def skill_proficiencies(cls, charID):
        questions = [
        inquirer.Checkbox('option',
                      message = "Which skills would you like to be proficient in (Pick 2)",
                      choices = ["acrobatics", "animal handling", "athletics", "history", "insight", "intimidation", "perception", "survival"],
                      ),
        ]
        answer = inquirer.prompt(questions)
        if len(answer["option"]) == 2:
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][0]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][1]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
        elif len(answer["option"]) > 2:
            print("Only Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 2:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)

# In Progress  
class Monk():
    hit_dice_val = 8

    @classmethod
    def start_proficencies(cls, charID):
        
        shields = CharProficiencies(charID, 80)
        simpleWeapons = CharProficiencies(charID, 84)
        martialWeapons = CharProficiencies(charID, 53)

        instruments = Proficiencies.get_by_type("Musical Instruments")
        art_tools = Proficiencies.get_by_type("Artisan's Tools")
        inst_tool_list = [instrument[1] for instrument in instruments]
        inst_tool_list.extend([tool[1] for tool in art_tools])


        questions = [
        inquirer.List('option',
                      message = "Which instrument or artisan tool would you like to be proficient in",
                      choices = inst_tool_list,
                      ),
        ]
        answer = inquirer.prompt(questions)
        for inst_tool in answer["option"]:
            for instrument in instruments:
                if inst_tool == instrument[1]:
                    CharProficiencies(charID, instrument[0])
            for art_tool in art_tools:
                if inst_tool == art_tool[1]:
                    CharProficiencies(charID, art_tool[0]) 
         
    
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
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][0]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
            sql = f'''
                    UPDATE characters
                    SET proficient = {True}
                    WHERE character_rel = {charID} AND skill = {answer["option"][1]}
                '''
            CURSOR.execute(sql)
            CONN.commit()
        elif len(answer["option"]) > 2:
            print("Only Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
        elif len(answer["option"]) < 2:
            print("Please Pick 2 Options!")
            time.sleep(2)
            Barbarian.skill_proficiencies(charID)
    
# class Barbarian():
#     hit_dice_val = 12

#     @classmethod
#     def start_proficencies(cls, charID):
#         lightArmor = CharProficiencies(charID, 46)
#         mediumArmor = CharProficiencies(charID, 56)
#         shields = CharProficiencies(charID, 80)
#         simpleWeapons = CharProficiencies(charID, 84)
#         martialWeapons = CharProficiencies(charID, 53)
    
#     @classmethod
#     def skill_proficiencies(cls, charID):
#         questions = [
#         inquirer.Checkbox('option',
#                       message = "Which skills would you like to be proficient in (Pick 2)",
#                       choices = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"],
#                       ),
#         ]
#         answer = inquirer.prompt(questions)
#         if len(answer["option"]) == 2:
#             sql = f'''
#                     UPDATE characters
#                     SET proficient = {True}
#                     WHERE character_rel = {charID} AND skill = {answer["option"][0]}
#                 '''
#             CURSOR.execute(sql)
#             CONN.commit()
#             sql = f'''
#                     UPDATE characters
#                     SET proficient = {True}
#                     WHERE character_rel = {charID} AND skill = {answer["option"][1]}
#                 '''
#             CURSOR.execute(sql)
#             CONN.commit()
#         elif len(answer["option"]) > 2:
#             print("Only Pick 2 Options!")
#             time.sleep(2)
#             Barbarian.skill_proficiencies(charID)
#         elif len(answer["option"]) < 2:
#             print("Please Pick 2 Options!")
#             time.sleep(2)
#             Barbarian.skill_proficiencies(charID)
    
# class Barbarian():
#     hit_dice_val = 12

#     @classmethod
#     def start_proficencies(cls, charID):
#         lightArmor = CharProficiencies(charID, 46)
#         mediumArmor = CharProficiencies(charID, 56)
#         shields = CharProficiencies(charID, 80)
#         simpleWeapons = CharProficiencies(charID, 84)
#         martialWeapons = CharProficiencies(charID, 53)
    
#     @classmethod
#     def skill_proficiencies(cls, charID):
#         questions = [
#         inquirer.Checkbox('option',
#                       message = "Which skills would you like to be proficient in (Pick 2)",
#                       choices = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"],
#                       ),
#         ]
#         answer = inquirer.prompt(questions)
#         if len(answer["option"]) == 2:
#             sql = f'''
#                     UPDATE characters
#                     SET proficient = {True}
#                     WHERE character_rel = {charID} AND skill = {answer["option"][0]}
#                 '''
#             CURSOR.execute(sql)
#             CONN.commit()
#             sql = f'''
#                     UPDATE characters
#                     SET proficient = {True}
#                     WHERE character_rel = {charID} AND skill = {answer["option"][1]}
#                 '''
#             CURSOR.execute(sql)
#             CONN.commit()
#         elif len(answer["option"]) > 2:
#             print("Only Pick 2 Options!")
#             time.sleep(2)
#             Barbarian.skill_proficiencies(charID)
#         elif len(answer["option"]) < 2:
#             print("Please Pick 2 Options!")
#             time.sleep(2)
#             Barbarian.skill_proficiencies(charID)
    
