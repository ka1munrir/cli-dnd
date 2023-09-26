from .init import CONN, CURSOR

class Spells:

    def __init__(self, name, level, school, ritual, components, materials, casting_time, dist, duration, desc) -> None:
        self.name = name
        self.level = level
        self.school = school
        self.ritual = ritual
        self.components = components
        self.materials = materials
        self.castings_time = casting_time
        self.dist = dist
        self.duration = duration
        self.desc = desc

    def __str__(self) -> str:
        return f""" Name: {self.name}
                    Level: {self.level}
                    School: {self.school}
                    Ritual: {self.ritual}
                    Components: {self.components}
                    Materials: {self.materials}
                    Casting Time: {self.casting_time}
                    Range: {self.dist}
                    Duration: {self.duration}
                    Description: {self.desc}
                """
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("name must be a string")
    name = property(get_name, set_name)
    def get_level(self):
        return self._level
    def set_level(self, level):
        if isinstance(level, int):
            self._level = level
        else:
            raise Exception("level must be an integer")
    level = property(get_level, set_level)
    def get_school(self):
        return self._school
    def set_school(self, school):
        if isinstance(school, str):
            self._school = school
        else:
            raise Exception("school must be a string")
    school = property(get_school, set_school)
    def get_ritual(self):
        return self._ritual
    def set_ritual(self, ritual):
        if ritual: 
            self._ritual = 1
        else:
            self._ritual = 0
    ritual = property(get_ritual, set_ritual)
    def get_components(self):
        return self._components
    def set_components(self, components):
        if isinstance(components, str):
            self._components = components
        else:
            raise Exception("Components must be a string")
    components = property(get_components, set_components)
    def get_materials(self):
        return self._materials
    def set_materials(self, materials):
        if isinstance(materials, str):
            self._materials = materials
        else:
            raise Exception("materials must be a string")
    materials = property(get_materials, set_materials)
    def get_casting_time(self):
        return self._casting_time
    def set_casting_time(self, casting_time):
        if isinstance(casting_time, str):
            self._casting_time = casting_time
        else:
            raise Exception("Casting time must be a string")
    casting_time = property(get_casting_time, set_casting_time)
    def get_dist(self):
        return self._dist
    def set_dist(self, dist):
        if isinstance(dist, int):
            self._dist = dist
        else:
            raise Exception("Dist must be an integer in terms of ft")
    dist = property(get_dist, set_dist)
    def get_duration(self):
        return self._duration
    def set_duration(self, duration):
        if isinstance(duration, str):
            self._duration = duration
        else:
            raise Exception("Duration must be a string")
    duration = property(get_duration, set_duration)
    def get_desc(self):
        return self._desc
    def set_desc(self, desc):
        if isinstance(desc, str):
            self._desc = desc
        else:
            raise Exception("Duration must be a string")
    desc = property(get_desc, set_desc)
    
