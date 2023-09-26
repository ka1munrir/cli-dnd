from .init import CONN, CURSOR

class CharSkills:

    def __init__(self, character_rel, skill, value, proficient, joat):
        self.character_rel = character_rel
        self.skill = skill
        self.value = value
        self.proficient = proficient
        self.joat = joat
    
    def __str__(self):
        return f"{self.skill.capitalize()}: {self.value} Proficient: {self.proficient} JOAT: {self.joat}"
    
    def _get_character_rel(self):
        return self._character_rel
    def _set_character_rel(self, character_rel):
        self._character_rel = character_rel
    character_rel = property(_get_character_rel, _set_character_rel)
    def _get_skill(self):
        return self._skill
    def _set_skill(self, skill):
        self._skill = skill
    skill = property(_get_skill, _set_skill)
    def _get_value(self):
        return self._value
    def _set_value(self, value):
        self._value = value
    value = property(_get_value, _set_value)
    def _get_proficient(self):
        return self._proficient
    def _set_proficient(self, proficient):
        self._proficient = proficient
    proficient = property(_get_proficient, _set_proficient)
    def _get_joat(self):
        return self._joat
    def _set_joat(self, joat):
        self._joat = joat
    joat = property(_get_joat, _set_joat)