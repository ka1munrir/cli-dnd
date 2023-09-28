import os
from spells import Spells
from proficiencies import Proficiencies

os.system("sqlite3 lib/database.db < lib/models/seed.sql")


Spells.fill()
Proficiencies.fill()