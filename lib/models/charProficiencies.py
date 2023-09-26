from .init import CONN, CURSOR

class CharProficiencies:

    def __init__(self, character_rel, name, desc) -> None:
        self.character_rel = character_rel
        self.name = name
        self.desc = desc

    def __str__(self) -> str:
        return f"<{self.character_rel} {self.name}: {self.description}>"
    
    def _get_character_rel(self):
        return self._character_rel
    def _set_character_rel(self, character_rel):
        if isinstance(character_rel, int):
            self._character_rel = character_rel
        else:
            raise Exception("character_rel must be an integer")
    character_rel = property(_get_character_rel, _set_character_rel)
    def _get_name(self):
        return self._name
    def _set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("name must be a string")
    name = property(_get_name, _set_name)
    def _get_desc(self):
        return self._desc
    def _set_desc(self, desc):
        if isinstance(desc, str):
            self._desc = desc
        else:
            raise Exception("desc must be a string")
    desc = property(_get_desc, _set_desc)