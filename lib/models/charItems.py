from .init import CONN, CURSOR

class CharItems:
    DAMAGE_TYPES = ["acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic", "piercing", "poison", "psychic", "radiant", "slashing", "thunder", None]
    
    def __init__(self, character_rel, name, kind, desc, cost, weight, damage, damage_type, dist) -> None:
        self.character_rel = character_rel
        self.name = name
        self.kind = kind
        self.desc = desc
        self.cost = cost
        self.weight = weight
        self.damage = damage
        self.damage_type = damage_type
        self.dist = dist
    
    def __str__(self) -> str:
        return f'''
                <Item: {self.name}\n
                 Owner: {self.character_rel}\n
                 type: {self.kind}\n
                 description: {self.desc}\n
                 cost: {self.cost} gp\n
                 weight: {self.weight}\n
                 damage: {self.damage}\n
                 damage_type: {self.damage_type}\n
                 range: {self.dist}\n
                >
                '''
    
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
    def _get_kind(self):
        return self._kind
    def _set_kind(self, kind):
        if isinstance(kind, str): 
            self._kind = kind
        else:
            raise Exception("kind must be a string")
    kind = property(_get_kind, _set_kind)
    def _get_desc(self):
        return self._desc
    def _set_desc(self, desc):
        if isinstance(desc, str):
            self._desc = desc
        else:
            raise Exception("desc must be a string")
    desc = property(_get_desc, _set_desc)
    def _get_cost(self):
        return self._cost
    def _set_cost(self, cost):
        if isinstance(cost, float):
            self._cost = cost
        else:
            raise Exception("cost must be a float")
    cost = property(_get_cost, _set_cost)
    def _get_weight(self):
        return self._weight
    def _set_weight(self, weight):
        if isinstance(weight, float):
            self._weight = weight
        else:
            raise Exception("cost must be a float")
    weight = property(_get_weight, _set_weight)
    def _get_damage(self):
        return self._damage
    def _set_damage(self, damage):
        if isinstance(damage, str):
            if len(damage.split('d')) != 2 and damage.split('d')[0].isdecimal() and damage.split('d')[1].isdecimal():
                self._damage = damage
            else:
                raise Exception('Damage must be in the format [number]d[number] ex: 1d4')
        else:
            raise Exception("damage must be a string")
    damage = property(_get_damage, _set_damage)
    def _get_damage_type(self):
        return self._damage_type
    def _set_damage_type(self, damage_type):
        if damage_type in self.DAMAGE_TYPES:
            self._damage_type = damage_type
        else:
            raise Exception("damage type must either be empty or a recognized DnD damage type")
    damage_type = property(_get_damage_type, _set_damage_type)
    def _get_dist(self):
        return self._dist
    def _set_dist(self, dist):
        if isinstance(dist, int):
            self._dist = dist
        else:
            raise Exception("range must be an integer ex: 5 for touch or 5ft")
    dist = property(_get_dist, _set_dist)

