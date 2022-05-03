game = TheThreeGame()

# Player 2 Winner
print('First_player: First_Turn')
print(game.make_move('first_player', 1))
print(game.get_moves('first_player'))
print(game.get_score('first_player'))
print(game.get_num_bank())

print('\nSecond_Player: Second_Turn')
print(game.make_move('second_player', 7))
print(game.get_moves('second_player'))
print(game.get_score('second_player'))
print(game.get_num_bank())

print('\nFirst_player: Third_Turn')
print(game.make_move('first_player', 3))
print(game.get_moves('first_player'))
print(game.get_score('first_player'))
print(game.get_num_bank())

print('\nSecond_Player: Fourth_Turn')
print(game.make_move('second_player', 6))
print(game.get_moves('second_player'))
print(game.get_score('second_player'))
print(game.get_num_bank())

print('\nFirst_player: Fifth_Turn')
print(game.make_move('first_player', 4))
print(game.get_moves('first_player'))
print(game.get_score('first_player'))
print(game.get_num_bank())

print('\nSecond_Player: Sixth_Turn')
print(game.make_move('second_player', 2))
print(game.get_moves('second_player'))
print(game.get_score('second_player'))
print(game.get_num_bank())

print('\nWinner')
print(game.get_winner())
print(game.is_it_a_draw())