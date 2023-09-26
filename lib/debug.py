from models.players import Players

player1 = Players("player1", "player1")
beep = Players("beep", "beep")
Players.get_player_by_username("beep")
print(Players.get_player_by_username("beep"))