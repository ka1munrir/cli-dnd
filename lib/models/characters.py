from .init import CONN, CURSOR

class Characters:

    def __init__(self, player_rel, name, race, job, level, proficiency, passive_perception, armor_class, speed, hit_points, temp_hit_points, hit_dice):
        self.player_rel = player_rel
        self.name = name
        self.race = race
        self.job = job
        self.level = level
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
        self._player_rel = player_rel
    player_rel = property(_get_player_rel, _set_player_rel)
    def _get_name(self):
        return self._name
    def _set_name(self, name):
        self._name = name
    name = property(_get_name, _set_name)
    def _get_race(self):
        return self._race
    def _set_race(self, race):
        self._race = race
    race = property(_get_race, _set_race)
    def _get_job(self):
        return self._job
    def _set_job(self, job):
        self._job = job
    job = property(_get_job, _set_job)
    def _get_level(self):
        return self._level
    def _set_level(self, level):
        self._level = level
    level = property(_get_level, _set_level)
    def _get_proficiency(self):
        return self._proficiency
    def _set_proficiency(self, proficiency):
        self._proficiency = proficiency
    proficiency = property(_get_proficiency, _set_proficiency)
    def _get_passive_perception(self):
        return self._passive_perception
    def _set_passive_perception(self, passive_perception):
        self._passive_perception = passive_perception
    passive_perception = property(_get_passive_perception, _set_passive_perception)
    def _get_armor_class(self):
        return self._armor_class
    def _set_armor_class(self, armor_class):
        self._armor_class = armor_class
    armor_class = property(_get_armor_class, _set_armor_class)
    def _get_speed(self):
        return self._speed
    def _set_speed(self, speed):
        self._speed = speed
    speed = property(_get_speed, _set_speed)
    def _get_hit_points(self):
        return self._hit_points
    def _set_hit_points(self, hit_points):
        self._hit_points = hit_points
    hit_points = property(_get_hit_points, _set_hit_points)
    def _get_temp_hit_points(self):
        return self._temp_hit_points
    def _set_temp_hit_points(self, temp_hit_points):
        self._temp_hit_points = temp_hit_points
    temp_hit_points = property(_get_temp_hit_points, _set_temp_hit_points)
    def _get_hit_dice(self):
        return self._hit_dice
    def _set_hit_dice(self, hit_dice):
        self._hit_dice = hit_dice
    hit_dice = property(_get_hit_dice, _set_hit_dice)

    def save(self):
        sql = f'''
        INSERT INTO characters (player_rel, name, race, job, level, proficiency, passive_perception, armor_class, speed, hit_points, temp_hit_points, hit_dice)
        VALUES ("{self.player_rel}", "{self.name}", "{self.race}", "{self.job}", "{self.level}", "{self.proficiency}", "{self.passive_perception}", "{self.armor_class}", "{self.speed}", "{self.hit_points}", "{self.temp_hit_points}", "{self.hit_dice}")
        '''
        CURSOR.execute(sql)
        CONN.commit()

    

    


    
        
