game = TheThreeGame()
print(game.make_move('first_player', 2))
print(game.make_move('second_player', 5))
print(game.make_move('first_player', 7))
print(game.get_winner())  # Should Return None
print(game.is_it_a_draw())  # Should Return 'GAME_UNFINISHED'