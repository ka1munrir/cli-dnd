from .init import CONN, CURSOR


class CharAttributes:
    
    def __init__(self, character_rel, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.character_rel = character_rel
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    
    def __str__(self) -> str:
        return f'''
                Attributes:\n
                Strength: {self.strength}\n
                Dexterity: {self.dexterity}\n
                Constitution: {self.constitution}\n
                Intelligence: {self.intelligence}\n
                Wisdom: {self.wisdom}\n
                Charisma: {self.charisma}\n
                '''
    
    def _get_character_rel(self):
        return self._character_rel
    def _set_character_rel(self, character_rel):
        self._character_rel = character_rel
    character_rel = property(_get_character_rel, _set_character_rel)
    def _get_strength(self):
        return self._strength
    def _set_strength(self, strength):
        self._strength = strength
    strength = property(_get_strength, _set_strength)
    def _get_dexterity(self):
        return self._dexterity
    def _set_dexterity(self, dexterity):
        self._dexterity = dexterity
    dexterity = property(_get_dexterity, _set_dexterity)
    def _get_constitution(self):
        return self._constitution
    def _set_constitution(self, constitution):
        self._constitution = constitution
    constitution = property(_get_constitution, _set_constitution)
    def _get_intelligence(self):
        return self._intelligence
    def _set_intelligence(self, intelligence):
        self._intelligence = intelligence
    intelligence = property(_get_intelligence, _set_intelligence)
    def _get_wisdom(self):
        return self._wisdom
    def _set_wisdom(self, wisdom):
        self._wisdom = wisdom
    wisdom = property(_get_wisdom, _set_wisdom)
    def _get_charisma(self):
        return self._charisma
    def _set_charisma(self, charisma):
        self._charisma = charisma
    charisma = property(_get_charisma, _set_charisma)
