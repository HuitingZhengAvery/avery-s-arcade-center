from tiles import Tiles
import time


class Board:
    '''The game board that displays the on-going game'''
    def __init__(self, WIDTH, HEIGHT, GRID, game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.GRID = GRID
        self.row = self.HEIGHT // self.GRID
        self.centre = self.GRID // 2
        self.gc = game_controller

        # Initial tile numbers
        self.black = 0
        self.white = 0

        # Controls each player's turn to make a move
        self.whiteTurn = False

        # The game board as a nested list
        self.table = []
        self.available = []
        for i in range(1, self.row + 1):
            self.available.append(i)
            self.table.append([i for i in
                              range(1, self.WIDTH // self.GRID + 1)])
        self.tiles = Tiles(self.GRID, self.table)

        # 8 directions for seaching legal moves and flipping
        self.ROW_VEC = [1, -1, 0, 0, -1, 1, -1, 1]
        self.COL_VEC = [0, 0, -1, 1, -1, -1, 1, 1]

        self.flip_time = 0
        self.gc.end_time = self.flip_time

    def update(self):
        '''Controls the game's status'''
        self.tiles.display()
        if (self.black + self.white == self.row ** 2) or\
           (len(self.legalMoves("B", "W")) == 0 and
           len(self.legalMoves("W", "B")) == 0):
            self.gc.game_ends = True
            self.gc.num = max(self.black, self.white)
            self.gc.black = self.black
            if self.black > self.white:
                self.gc.black_wins = True
            elif self.white > self.black:
                self.gc.white_wins = True
            else:
                self.gc.tie = True

        if self.whiteTurn is True:
            # Provides a 800 millisecond delay for the computer's move
            if millis() > self.flip_time + 800:
                self.pcMove()

    def begin(self):
        '''Setup initial 4 tiles'''
        left_and_up = self.row // 2 - 1
        right_and_down = self.row // 2
        self.table[left_and_up][left_and_up] = "W"
        self.table[right_and_down][right_and_down] = "W"
        self.table[left_and_up][right_and_down] = "B"
        self.table[right_and_down][left_and_up] = "B"
        print("Your turn")

    def pcMove(self):
        '''Lets the computer make its move'''
        legal_move = self.legalMoves("W", "B")

        # If there is no legal move for the computer, switch to
        # the player's turn
        if len(legal_move) == 0:
            self.whiteTurn = False
        else:
            indicator = sorted(
                legal_move.items(),
                key=lambda x: x[1],
                reverse=True
            )
            # Take the move that can flip most tiles
            best_move = indicator[0][0]
            row = best_move[0]
            column = best_move[1]
            self.table[row][column] = "W"
            self.flip(row, column, "W")
            self.whiteTurn = False
            print("Your turn")

    def playerMove(self, mouseX, mouseY):
        '''Lets the player make a legal move upon each mouse click'''
        legal_move = self.legalMoves("B", "W")
        if len(legal_move) == 0:
            self.whiteTurn = True
        row = mouseY // self.GRID
        column = mouseX // self.GRID
        if (row, column) in legal_move:
            self.table[row][column] = "B"
            self.flip(row, column, "B")
            self.whiteTurn = True
            print("Computer's turn")

    def legalMoves(self, color, other):
        '''Searches the game board for all legal moves'''
        # A dictionary that records each legal
        # move's position and the number of tiles it can flip
        legal_list = {}

        for row in range(len(self.table)):
            for column in range(len(self.table[row])):

                # Find the tile with targeted color
                if self.table[row][column] == color:

                    # Check legal moves in 8 directions
                    for i in range(len(self.ROW_VEC)):
                        can_flip = []
                        new_row = row + self.ROW_VEC[i]
                        new_col = column + self.COL_VEC[i]

                        # Exclude directions with no legal move
                        if not self.on_board(new_row, new_col) or\
                           self.table[new_row][new_col] in self.available or\
                           self.table[new_row][new_col] == color:
                            continue

                        # Record tiles that could be flipped
                        while self.on_board(new_row, new_col) and\
                                self.table[new_row][new_col] == other:
                            can_flip.append((new_row, new_col))
                            new_row += self.ROW_VEC[i]
                            new_col += self.COL_VEC[i]

                        # The space is a legal move only if it reaches
                        # an empty space at the end
                        if self.on_board(new_row, new_col) and\
                           self.table[new_row][new_col] in self.available:
                            if (new_row, new_col) in legal_list:
                                legal_list[(new_row, new_col)] += len(can_flip)
                            else:
                                legal_list[(new_row, new_col)] = len(can_flip)

        return legal_list

    def flip(self, row, column, color):
        '''Flips tiles after a legal move'''

        # millis() is not a Python function and will cause test
        # error when running pytest, please comment this line before
        # testing.
        self.flip_time = millis()

        # Search in 8 directions
        for i in range(len(self.ROW_VEC)):
            # Potential tiles that could be flipped
            can_flip = []
            new_row = row + self.ROW_VEC[i]
            new_col = column + self.COL_VEC[i]
            if not self.on_board(new_row, new_col) or\
               self.table[new_row][new_col] in self.available or\
               self.table[new_row][new_col] == color:
                continue
            else:
                while self.on_board(new_row, new_col) and\
                      self.table[new_row][new_col] != color and \
                      self.table[new_row][new_col] not in self.available:
                    can_flip.append((new_row, new_col))
                    new_row += self.ROW_VEC[i]
                    new_col += self.COL_VEC[i]
                if self.on_board(new_row, new_col) and\
                   self.table[new_row][new_col] == color:
                    for to_flip in can_flip:
                        self.table[to_flip[0]][to_flip[1]] = color

        # Update tile_numbers after each flip
        self.tile_numbers()

    def on_board(self, row, column):
        '''Returns a boolean value on whether the space is within the board'''
        if row >= 0 and column >= 0 and row < self.HEIGHT // self.GRID\
           and column < self.WIDTH // self.GRID:
            return True
        return False

    def tile_numbers(self):
        '''Updates the current tile numbers upon each call'''
        self.black = 0
        self.white = 0
        for i in self.table:
            for j in i:
                if j == "B":
                    self.black += 1
                elif j == "W":
                    self.white += 1
