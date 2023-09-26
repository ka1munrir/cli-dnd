from .init import CONN, CURSOR

class CharSpells:

    def __init__(self, character_rel, spell_rel) -> None:
        self.character_rel = character_rel
        self.spell_rel = spell_rel
    
    def __str__(self) -> str:
        return f"<Character {self.character_rel} Spell: {self.spell_rel}>"
    
    def _get_character_rel(self):
        return self._character_rel
    def _set_character_rel(self, character_rel):
        if isinstance(character_rel, int):
            self._character_rel = character_rel
        else:
            raise Exception("character_rel must be an integer")
    character_rel = property(_get_character_rel, _set_character_rel)
    def _get_spell_rel(self):
        return self._spell_rel
    def _set_spell_rel(self, spell_rel):
        if isinstance(spell_rel, int):
            self._spell_rel = spell_rel
        else:
            raise Exception("spell_rel must be an integer")
    spell_rel = property(_get_spell_rel, _set_spell_rel)