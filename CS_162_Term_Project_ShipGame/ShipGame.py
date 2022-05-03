# Author: Angela Montez
# Github username: almontez
# Date: 03/08/2022
# Description: Simulates a pared down version of battleship, wherein two players can place ships on their
#              respective boards and then fire torpedoes at their opponent's ships.
#
#              Rules: ShipGame is a 2 player game with two distinct phases.
#              Phase 1: The first phase is the place ships phase. During this phase, players can place
#              ships on their board. Ships must be a minimum of size of 2 and a maximum size of 10.
#              Ships must fit on the board and cannot overlap.
#              Phase 2: The second phase is the torpedo phase. Player turns are enforced in this phase.
#              A turn consists of a player firing a torpedo at their opponent's ship. The 'first' player goes first.
#              Win Conditions: Player must sink all of opponent's ships.

class MapKey:
    """Represents a map legend or key for all x, y coordinates on the board. Critical part of program used in
       all other classes. Example: {'A1': (0, 0), 'A2': (0, 1), 'A3': (0, 2),...}"""

    def __init__(self):
        """Constructs a dictionary with all the x,y coordinates on the board identified by their row/column headers"""
        coord_dict = {}

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        for row in range(10):
            for col in range(10):
                key = letters[row] + numbers[col]
                coord_dict[key] = (row, col)

        self._map_key = coord_dict

    def get_map(self):
        """Returns a dictionary with all the x,y coordinates on the board identified by their row/column headers"""
        return self._map_key


class Board:
    """Represents a 10x10 game board. Each player should have their own game board"""

    def __init__(self):
        """Creates a dictionary that represents the board"""
        coord_status_dict = {}

        for row in range(10):
            for col in range(10):
                coord_status_dict[(row, col)] = 'O'

        self._board = coord_status_dict     # actual game board
        self._coord_key = MapKey()          # from MapKey class: used in translating row/col input to x,y coord.

    def validate_fit(self, ship_size, ship_location, ship_orientation):
        """Checks if new ship will fit on board without overlapping any previously placed ships
           Returns True if ship will fit. Returns False is ship will not fit. Called within place_ship
           method of ShipGame class"""

        # ships represented as X on board
        ship_text = 'X'

        # get x,y coordinates of ship head
        coord_map = self._coord_key.get_map()
        start_coord = coord_map[ship_location]
        row, col = start_coord

        # determine if ship fits on board at starting position
        subtract_value = row         # value used when orientation = C
        if ship_orientation.upper() == 'R':
            subtract_value = col     # value used when orientation = R
        space_available = 10 - subtract_value
        if space_available < ship_size:
            return False

        # determine if new ship will overlap with existing ships
        for pos in range(ship_size):
            if self._board[(row, col)] == ship_text:
                return False

            # move to next coordinate based on orientation
            if ship_orientation.upper() == 'C':
                row += 1
            elif ship_orientation.upper() == 'R':
                col += 1

        return True

    def add_ship_to_board(self, ship):
        """Updates player board by adding a ship. Called from within place_ship method of ShipGame class"""
        # ships represented as X on board
        ship_text = 'X'

        # list of ship pieces
        ship_pieces = ship.get_ship()

        # add ship pieces to board
        for coordinates in ship_pieces:
            self._board[coordinates] = ship_text

    def record_attack(self, target):
        """Updates opponent's board after a torpedo has been fired. Called from within fire_torpedo method of
           ShipGame class"""
        # torpedoes represented as H on board
        hit = 'H'

        # ships represented as X on board
        ship_text = 'X'

        # get x,y coordinates of target
        coord_map = self._coord_key.get_map()
        coordinate = coord_map[target]

        # update board with a hit
        if self._board[coordinate] == ship_text:
            # torpedo hit a ship
            self._board[coordinate] = hit
            return True
        else:
            # torpedo did not hit a ship
            self._board[coordinate] = hit
            return False

    def print_game_board(self):
        """Displays game board. Called from within view_player_board method of ShipGame class."""
        let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        # print column headers [1 - 10]
        print(end='       ')    # used to align column headers
        for col in range(10):
            print(num[col], end='      ')
        print('\n')

        for row in range(10):
            # print row headers [A - J]
            print(let[row], end='      ')

            # print grid
            for col in range(10):
                print(self._board[row, col], end='      ')
            print('\n')

        return "Board Printed"


class Ship:
    """Ship object with a size, location, and orientation"""

    def __init__(self, ship_size, ship_location, ship_orientation):
        """Construct Ship Object"""
        self._size = ship_size
        self._location = ship_location           # only reference head of ship [Ex: A1]; not all of ship
        self._orientation = ship_orientation     # R = Row[Horizontal], C = Column[Vertical]
        self._map_key = MapKey()                 # from MapKey class: used in constructing ship
        self._ship = self.build_ship()           # holds all coordinates that makes up ship

    def build_ship(self):
        """Build ship: Add all coordinates of ship to ship list. Returns ship_pieces as a list to self._ship
           Called when ship is being constructed [see init in ship class and place_ship method in ShipGame class"""
        ship_pieces = []

        # get x,y coordinates of ship head
        parts = self._map_key.get_map()
        start_coordinates = parts[self._location]

        # determine loop count and variables
        length = self._size
        row, col = start_coordinates

        # build ship of variable size given orientation
        for pos in range(length):
            coordinates = (row, col)
            ship_pieces.append(coordinates)

            # move to next coordinate based on orientation
            if self._orientation.upper() == 'C':
                row += 1
            elif self._orientation.upper() == 'R':
                col += 1

        return ship_pieces

    def remove_ship_piece(self, target):
        """Represents a ship piece being hit. Removes coordinate of ship from ship list.
           Called from within update_player_ship method of ShipGame class"""
        if target in self._ship:
            self._ship.remove(target)

    def get_ship_size(self):
        """Returns the size/length of a player's ship"""
        return self._size

    def get_ship_location(self):
        """Returns the initial location of a player's ship [i.e. head of the ship]. """
        return self._location

    def get_ship_orientation(self):
        """Returns the orientation of a player's ship.
           Orientation can be horizontal[R] or vertical[C]"""
        return self._orientation

    def get_ship(self):
        """Returns a list of all the coordinates of a ship"""
        return self._ship


class ShipGame:
    """Simulates a simplified version of the game Battleship"""

    def __init__(self):
        """Initialize ShipGame data members"""
        self._turn = 'first'
        self._state = 'UNFINISHED'              # states = 'FIRST_WON', 'SECOND_WON', 'UNFINISHED'

        self._player1_board = Board()           # create player 1 board
        self._player1_ships = []                # hold player 1 ship objects

        self._player2_board = Board()           # create player 2 board
        self._player2_ships = []                # hold player 2 ship objects

        self._map_key = MapKey()                # from MapKey class: used in translating row/col input to x,y coord.

    def place_ship(self, player, ship_size, ship_location, ship_orientation):
        """Adds a ship of a given size and orientation to a specified location on the player's board"""

        # min size of ship is length 2
        # max size of ship is length 10 [size of board]
        if ship_size < 2 or ship_size > 10:
            return False

        # check coordinate is on map
        is_valid_coord = self.valid_coord(ship_location)
        if not is_valid_coord:
            return False

        # set variables for player board and ship holdings
        board = self._player1_board
        ship_holdings = self._player1_ships
        if player == 'second':
            board = self._player2_board
            ship_holdings = self._player2_ships

        # validate ship will fit on board without overlaps
        is_valid = board.validate_fit(ship_size, ship_location, ship_orientation)

        # add ship to player's board and holdings
        if is_valid:
            new_ship = Ship(ship_size, ship_location, ship_orientation)    # create ship
            board.add_ship_to_board(new_ship)   # add ship to board
            ship_holdings.append(new_ship)      # add ship to player's holdings
            return True
        else:
            return False

    def fire_torpedo(self, player, target):
        """Fires a torpedo at opponent's ship."""

        # confirm game has not already been won by a player
        if self._state != 'UNFINISHED':
            return False

        # confirm correct player turn
        is_valid_turn = self.valid_move(player)
        is_valid_coord = self.valid_coord(target)

        # set variables for player board and holdings given valid turn
        if is_valid_turn and is_valid_coord:
            board = self._player2_board
            holdings = self._player2_ships
            if player == 'second':
                board = self._player1_board
                holdings = self._player1_ships
        else:
            return False

        # torpedo target: add hit to opponent's board
        is_hit = board.record_attack(target)

        if is_hit:
            # remove sunken ship parts from ship list
            self.update_player_ships(target, holdings)

        # remove sunken ships from opponent's holdings
        for ship in holdings:
            if not ship.get_ship():
                holdings.remove(ship)

            # check for win
            self.check_for_win(player)

        # update game turn
        self.update_turn(player)
        return True

    def update_player_ships(self, target, holdings):
        """Helper method for fire_torpedo: Updates pieces remaining of a player's ship after being hit"""
        # get user input as x,y coordinates
        coord_map = self._map_key.get_map()
        target_coord = coord_map[target]

        # set loop counter
        size = len(holdings)
        for idx in range(size):
            for ship in holdings:
                if target_coord in ship.get_ship():
                    ship.remove_ship_piece(target_coord)
                    return True

    def check_for_win(self, player):
        """Helper function for fire_torpedo: Checks to see if all opponent's ships have been sunk"""

        # get opponent's ships remaining
        result = self.get_num_ships_remaining('second')
        if player.lower() == 'second':
            result = self.get_num_ships_remaining('first')

        # if ship's remaining is zero, all opponent's ships sunk
        # player is the winner
        if result == 0:
            if player.lower() == 'first':
                self._state = 'FIRST_WON'
            else:
                self._state = 'SECOND_WON'
            return True

        # neither player has won: continue game
        return False

    def update_turn(self, player):
        """Helper function for fire_torpedo: Updates player turn"""
        self._turn = 'second'
        if player == 'second':
            self._turn = 'first'

    def valid_move(self, player):
        """Helper function for fire_torpedo: Validates if it is the correct player's turn"""
        # not player's turn
        if self._turn != player:
            return False
        # player's turn
        return True

    def valid_coord(self, coordinate):
        """Helper function for place_ship and fire_torpedo: Validates if coordinate is on board"""
        coord_map = self._map_key.get_map()
        if coordinate not in coord_map:
            return False
        return True

    def get_num_ships_remaining(self, player):
        """Returns the number of ships a player has remaining"""
        if player.lower() == 'first':
            player = self._player1_ships
        elif player.lower() == 'second':
            player = self._player2_ships

        return len(player)

    def get_current_state(self):
        """Returns the current state of the game. Game states include: 'FIRST_WON', 'SECOND_WON', 'UNFINISHED'"""
        return self._state

    def view_player_board(self, player):
        """Returns the board of a specified player in grid form"""

        # set up variables based on player
        message = 'Player 1 Board: Grid View'
        board = self._player1_board
        if player.lower() == 'second':
            message = 'Player 2 Board: Grid View'
            board = self._player2_board

        # display board
        print(message)
        board.print_game_board()
        return 'Board Printed'
