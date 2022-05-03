game = TheThreeGame()
print(game.make_move('first_player', 2))
print(game.make_move('first_player', 5))  # Should Return False
print(game.get_num_bank())
print(game.make_move('first_player', 7))
print(game.get_moves('first_player'))
print(game.get_score('first_player'))
print(game.get_num_bank())
print(game.get_winner())  # Should Return None
print(game.is_it_a_draw())  # Should Return 'GAME_UNFINISHED'