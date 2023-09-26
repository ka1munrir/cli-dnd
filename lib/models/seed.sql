DROP TABLE IF EXISTS charSpells;
DROP TABLE IF EXISTS charItems;
DROP TABLE IF EXISTS charProficiencies;
DROP TABLE IF EXISTS charSkills;
DROP TABLE IF EXISTS charSkillsConnect;
DROP TABLE IF EXISTS charAttributes;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS spells;

-- Table: players
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

-- Table: characters
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    player_rel INTEGER,
    name TEXT,
    race ENUM,
    class ENUM,
    level INTEGER,
    alignment ENUM,
    background TEXT,
    proficiency INTEGER,
    passive_perception INTEGER,
    armor_class INTEGER,
    speed INTEGER,
    hit_points INTEGER,
    temporary_hit_points INTEGER,
    hit_dice INTEGER,
    FOREIGN KEY (player_rel) REFERENCES players(id)
);

-- Table: charAttributes
CREATE TABLE IF NOT EXISTS charAttributes (
    id INTEGER PRIMARY KEY,
    character_rel INTEGER,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    FOREIGN KEY (character_rel) REFERENCES characters(id)
);

-- Table: charSkills
CREATE TABLE IF NOT EXISTS charSkills (
    id INTEGER PRIMARY KEY,
    character_rel INTEGER,
    skill ENUM,
    value INTEGER,
    proficient BOOL,
    joat BOOL,
    FOREIGN KEY (character_rel) REFERENCES characters(id)
);

-- Table: charProficiencies
CREATE TABLE IF NOT EXISTS charProficiencies (
    id INTEGER PRIMARY KEY,
    character_rel INTEGER,
    name TEXT,
    description TEXT,
    FOREIGN KEY (character_rel) REFERENCES characters(id)
);

-- Table: charItems
CREATE TABLE IF NOT EXISTS charItems (
    id INTEGER PRIMARY KEY,
    character_rel INTEGER,
    name TEXT,
    type ENUM,
    description TEXT,
    cost FLOAT,
    weight FLOAT,
    damage TEXT,
    damage_type ENUM,
    distance INTEGER,
    FOREIGN KEY (character_rel) REFERENCES characters(id)
);


-- Table: spells
CREATE TABLE IF NOT EXISTS spells (
    id INTEGER PRIMARY KEY,
    name TEXT,
    level INTEGER,
    school TEXT,
    ritual BOOL,
    concentration BOOL,
    components TEXT,
    materials TEXT,
    casting_time TEXT,
    distance TEXT,
    duration TEXT,
    description TEXT
);

-- Table: charSpells
CREATE TABLE IF NOT EXISTS charSpells (
    id INTEGER PRIMARY KEY,
    character_rel INTEGER,
    spell_rel INTEGER,
    FOREIGN KEY (character_rel) REFERENCES characters(id)
    FOREIGN KEY (spell_rel) REFERENCES spells(id)
);
