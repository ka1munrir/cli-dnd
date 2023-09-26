from .init import CURSOR, CONN

class Players:

    def __init__(self, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.save()

    def __str__(self) -> str:
        return f"<Player username: {self.username},  password: {self.password}>"
    
    def _get_username(self):
        return self._username
    def _set_username(self, username):
        if not Players.get_by_username(username):
            self._username = username
        else:
            raise Exception("Username is already taken")
    username = property(_get_username, _set_username)
    def _get_password(self):
        return self._password
    def _set_password(self, password):
        self._password = password
    password = property(_get_password, _set_password)

    def save(self):
        sql = f'''
        INSERT INTO players (username, password)
        VALUES ("{self.username}", "{self.password}")
        '''
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def get_by_username(cls, username):
        sql = f'''
        SELECT *
        FROM players
        WHERE username = "{username}"
        '''
        player = CURSOR.execute(sql).fetchone()
        return (player)




