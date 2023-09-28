from init import CONN, CURSOR
import requests, json

class Proficiencies():

    TYPES = ["Artisan's Tools", 'Armor', 'Musical Instruments', 'Weapons', 'Gaming Sets', 'Other', 'Vehicles', 'Saving Throws', 'Skills']

    @classmethod
    def fill(self):
        baseLink = 'https://www.dnd5eapi.co'

        res = requests.get(f'{baseLink}/api/proficiencies')
        r = json.loads(res.text)
        # ptypes = []
        for result in r["results"]:
            a = requests.get(f'{baseLink}{result["url"]}')
            b = json.loads(a.text)
            cr = []
            for c in b["classes"]:
                cr.append(c["index"])
            for r in b["races"]:
                cr.append(r["index"])
            sql = f'''
            INSERT INTO proficiencies (name, type, people)
            VALUES ("{b["name"].replace('"', "'")}", "{b["type"].replace('"', "'")}", "{", ".join(cr).replace('"', "'")}")
            '''
            # if b["type"] not in ptypes:
            #     ptypes.append(b["type"])
            CURSOR.execute(sql)
            CONN.commit()
        # print(ptypes)