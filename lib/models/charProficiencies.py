from .init import CONN, CURSOR

class CharProficiencies:

    def __init__(self, character_rel, proficiencies_rel) -> None:
        self.character_rel = character_rel
        self.proficiencies_rel = proficiencies_rel
        self.save()

    def __str__(self) -> str:
        return f"<{self.character_rel} {self.proficiencies_rel}>"
    
    def _get_character_rel(self):
        return self._character_rel
    def _set_character_rel(self, character_rel):
        if isinstance(character_rel, int):
            self._character_rel = character_rel
        else:
            raise Exception("character_rel must be an integer")
    character_rel = property(_get_character_rel, _set_character_rel)
    def _get_proficiencies_rel(self):
        return self._proficiencies_rel
    def _set_proficiencies_rel(self, proficiencies_rel):
        if isinstance(proficiencies_rel, int):
            self._proficiencies_rel = proficiencies_rel
        else:
            raise Exception("proficiencies_rel must be an integer")
    proficiencies_rel = property(_get_proficiencies_rel, _set_proficiencies_rel)

    def save(self):
        sql = f'''
        INSERT INTO charProficiencies (player_rel, proficiencies_rel)
        VALUES ("{self.character_rel}", "{self.proficiencies_rel}")
        '''
        CURSOR.execute(sql)
        CONN.commit()