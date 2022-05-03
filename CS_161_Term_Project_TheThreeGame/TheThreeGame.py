# Author: Angela Montez
# Date: 11/30/2021
# Course: CS 161, Fall 2021
# Description: Two-player game in which players alternately choose numbers from 1-9.
#               The winner of the game is to be the first player to with numbers that
#               sum to 15.

class TheThreeGame:
    """Blueprint for game including methods for tracking player turns, numbers guessed, state of the game, and winner"""

    def __init__(self):
        """Constructs players and players' guesses, score, and turn"""

        self._numbers_bank = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._num_turns = 0

        self._first_player = 'first_player'
        self._first_player_score = 0
        self._first_player_guess_bank = []

        self._second_player = 'second_player'
        self._second_player_score = 0
        self._second_player_guess_bank = []

    def get_moves(self, player):
        """Returns a list of the player's guesses """
        if player == 'first_player':
            return self._first_player_guess_bank
        elif player == 'second_player':
            return self._second_player_guess_bank

    def get_num_bank(self):
        """Returns numbers remaining in the number bank"""
        return self._numbers_bank

    def get_score(self, player):
        """Returns the sum of the player's guesses"""
        if player == 'first_player':
            return self._first_player_score
        elif player == 'second_player':
            return self._second_player_score

    def get_winner(self):
        """Returns winner of game"""
        if self._first_player_score == 15:
            return 'FIRST_PLAYER_WON'
        elif self._second_player_score == 15:
            return 'SECOND_PLAYER_WON'
        else:
            return None

    def is_it_a_draw(self):
        """Returns Draw when no winner or Game_Unfinished if unfinished"""
        if self._first_player_score == 15 or self._second_player_score == 15:
            return self.get_winner()
        elif not self._numbers_bank:
            return 'IT_IS_A_DRAW'
        else:
            return 'GAME_UNFINISHED'

    def validate_player(self, player):
        """Returns true if player's turn."""
        self._num_turns += 1

        if self._num_turns % 2 != 0 and player == 'first_player':
            return True
        elif self._num_turns % 2 == 0 and player == 'second_player':
            return True

    def validate_guess(self, guess):
        """Returns true if valid guess"""
        if guess not in self._numbers_bank or guess > 9 or guess < 1:
            return False
        else:
            return True

    def is_valid_move(self, player, guess):
        """Returns True if valid player turn and valid player guess"""
        if self.validate_player(player) and self.validate_guess(guess):
            return True
        else:
            self._num_turns -= 1
            return False

    def make_move(self, player, guess):
        """Logs valid player guesses if no winner or game unfinished"""

        if not self.get_winner():
            if self.is_it_a_draw() == 'GAME_UNFINISHED':
                if self.is_valid_move(player, guess):
                    if player == 'first_player':
                        self._first_player_guess_bank.append(guess)
                        self._first_player_score += guess
                        self._numbers_bank.remove(guess)
                        return True
                    elif player == 'second_player':
                        self._second_player_guess_bank.append(guess)
                        self._second_player_score += guess
                        self._numbers_bank.remove(guess)
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
