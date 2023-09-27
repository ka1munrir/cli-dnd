from .init import CONN, CURSOR

class Characters:
    RACES = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "half-orc", "halfling", "human", "tiefling"]
    CLASSES = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
    def __init__(self, player_rel, name, race, job, level, background, proficiency, passive_perception, armor_class, speed, hit_points, temp_hit_points, hit_dice):
        self.player_rel = player_rel
        self.name = name
        self.race = race
        self.job = job
        self.level = level
        self.background = background
        self.proficiency = proficiency
        self.passive_perception = passive_perception
        self.armor_class = armor_class
        self.speed = speed
        self.hit_points = hit_points
        self.temp_hit_points = temp_hit_points
        self.hit_dice = hit_dice
        self.save()

    def _get_player_rel(self):
        return self._player_rel
    def _set_player_rel(self, player_rel):
        if isinstance(player_rel, int):
            self._player_rel = player_rel
        else:
            raise Exception("Player_rel must be an integer")
    player_rel = property(_get_player_rel, _set_player_rel)
    def _get_name(self):
        return self._name
    def _set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("name must be a string")
    name = property(_get_name, _set_name)
    def _get_race(self):
        return self._race
    def _set_race(self, race):
        if race in self.RACES:
            self._race = race
        else:
            raise Exception("Race must be an official DnD race")
    race = property(_get_race, _set_race)
    def _get_job(self):
        return self._job
    def _set_job(self, job):
        if job in self.CLASSES:
            self._job = job
        else:
            raise Exception("Class must be an official DnD class")
    job = property(_get_job, _set_job)
    def _get_level(self):
        return self._level
    def _set_level(self, level):
        if isinstance(level, int):
            self._level = level
        else:
            raise Exception("Level must be an integer")
    level = property(_get_level, _set_level)
    def _get_background(self):
        return self._background
    def _set_background(self, background):
        if isinstance(background, str):
            self._background = background
        else:
            raise Exception("Background must be a string")
    background = property(_get_background, _set_background)
    def _get_proficiency(self):
        return self._proficiency
    def _set_proficiency(self, proficiency):
        if isinstance(proficiency, int):
            self._proficiency = proficiency
        else:
            raise Exception("character proficiency must be an integer")
    proficiency = property(_get_proficiency, _set_proficiency)
    def _get_passive_perception(self):
        return self._passive_perception
    def _set_passive_perception(self, passive_perception):
        if isinstance(passive_perception, int):
            self._passive_perception = passive_perception
        else:
            raise Exception("Passive perception must be an integer")
    passive_perception = property(_get_passive_perception, _set_passive_perception)
    def _get_armor_class(self):
        return self._armor_class
    def _set_armor_class(self, armor_class):
        if isinstance(armor_class, int):
            self._armor_class = armor_class
        else:
            raise Exception("Armor class must be an integer")
    armor_class = property(_get_armor_class, _set_armor_class)
    def _get_speed(self):
        return self._speed
    def _set_speed(self, speed):
        if isinstance(speed, int):
            self._speed = speed
        else:
            raise Exception("speed must be an integer")
    speed = property(_get_speed, _set_speed)
    def _get_hit_points(self):
        return self._hit_points
    def _set_hit_points(self, hit_points):
        if isinstance(hit_points, int):
            self._hit_points = hit_points
        else:
            raise Exception("Hit points must be an integer")
    hit_points = property(_get_hit_points, _set_hit_points)
    def _get_temp_hit_points(self):
        return self._temp_hit_points
    def _set_temp_hit_points(self, temp_hit_points):
        if isinstance(temp_hit_points, int):
            self._temp_hit_points = temp_hit_points
        else:
            raise Exception("temporary hit points must be an integer")
    temp_hit_points = property(_get_temp_hit_points, _set_temp_hit_points)
    def _get_hit_dice(self):
        return self._hit_dice
    def _set_hit_dice(self, hit_dice):
        if isinstance(hit_dice, int):
            self._hit_dice = hit_dice
        else:
            raise Exception("Hit dice value must be an integer")
    hit_dice = property(_get_hit_dice, _set_hit_dice)

    def save(self):
        sql = f'''
        INSERT INTO characters (player_rel, name, race, class, level, background, proficiency, passive_perception, armor_class, speed, hit_points, temporary_hit_points, hit_dice)
        VALUES ("{self.player_rel}", "{self.name}", "{self.race}", "{self.job}", "{self.level}", "{self.background}", "{self.proficiency}", "{self.passive_perception}", "{self.armor_class}", "{self.speed}", "{self.hit_points}", "{self.temp_hit_points}", "{self.hit_dice}")
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def get_by_user(cls, userID):
        sql = f'''
        SELECT *
        FROM characters
        WHERE player_rel = "{userID}"
        '''
        characters = CURSOR.execute(sql).fetchall()
        return (characters)
    
    @classmethod
    def get_by_id(cls, charID):
        sql = f'''
        SELECT *
        FROM characters
        WHERE id = "{charID}"
        '''
        character = CURSOR.execute(sql).fetchone()
        return (character)