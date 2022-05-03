# project-9

Write a class called TheThreeGame that allows two players to play a game in which they alternately choose numbers from 1-9.  They may not choose a number that has already been selected by either player.  If at any point exactly three of a player's numbers sum to exactly 15, then that player has won.  If all numbers from 1-9 are chosen, but neither player has won, then the game ends in a draw. Player "first_player" has the first turn.

The class will need **private** data members for:
1. keeping track of which numbers have been chosen, and by whom
2. the current state, which holds one of the four following values: "FIRST_PLAYER_WON", "SECOND_PLAYER_WON", "IT_IS_A_DRAW", or "GAME_UNFINISHED"
3. keeping track of whose turn it is

Your TheThreeGame class must include the following methods:
* An `__init__` method that takes no parameters and initializes all data members.
* A get method named `get_winner`, which returns "FIRST_PLAYER_WON" if first player has won, "SECOND_PLAYER_WON" if second player has won and `None` if no player has won. 
* A method named `is_it_a_draw` which returns "IT_IS_A_DRAW" if it's a draw, else returns "GAME_UNFINISHED". If a player has won and `is_it_a_draw` is called, then it should return "FIRST_PLAYER_WON" or "SECOND_PLAYER_WON" accordingly. 
* A method named `make_move` that takes two parameters - a string designating the player making the move, either "first_player" or "second_player", and an integer giving their number choice (in that order).  If it is not that player's turn, or if the integer is not in the correct range, or if that integer has already been chosen, or if the game has already been won or drawn, `make_move` should return False. You can assume the user chooses an integer, but if it's outside the range 1-9, `make_move` should return False. Otherwise, it should record the move, update the current state if the move caused a win or draw, update which player's turn it is, and return True.

For example, your class could be used as follows:
```
game = TheThreeGame()
game.make_move("first_player", 2)
game.make_move("second_player", 5)
result = game.make_move("first_player", 7)
player_won = game.get_winner() #will return None because no player has won yet.
draw = game.is_it_a_draw() #will return "GAME_UNFINISHED" because it is not a draw yet nor has any player won.
```

Don't know where to start? First try playing a few games on paper to get a feel for how the rules work. Next, try working on the easiest bits first - then you can cross them off and (hopefully) not have to think about them anymore. 

In this project, the easiest part is the `get_winner` method, which just needs to return the value of a data member. The next easiest part is the `__init__` method, which just needs to initialize all of the data members. Initializing data members isn't usually difficult, but first you'll have to decide what data members you want to use to keep track of things. 

Most of the work is in the `make_move` and `is_it_a_draw` method. Probably the most challenging part of the `make_move` method is checking (if the proposed move was valid) whether the state of the game has changed to a win or draw. That functionality will be the job of `is_it_a_draw` method. And `make_move` can call `is_it_a_draw` to determine it instead of duplicating the effort. 

The other parts of `make_move` are checking whether the proposed move is valid, recording the move (if it's valid), and **returning either True or False** as appropriate. Remember to test your functions as you go. Do NOT try to code it all at once and then start testing - that's a recipe for frustration, since it makes it much harder to track down bugs. Remember to plan out your tests ahead of time. If you don't know what result you should get before running a test, it can be easy to convince yourself that the result your program gives you looks okay.

Your file must be named: `TheThreeGame.py`
