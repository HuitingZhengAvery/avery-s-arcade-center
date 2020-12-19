from game_board import Board
from game_controller import GameController

# !!! Please comment "self.flip_time = millis()"
# under flip() method before testing


def test_constructor():
    gc = GameController(400, 400)
    new_board = Board(400, 400, 100, gc)
    assert new_board.WIDTH == 400
    assert new_board.HEIGHT == 400
    assert new_board.GRID == 100
    assert new_board.whiteTurn is False
    assert new_board.available == [1, 2, 3, 4]
    assert new_board.table == [[1, 2, 3, 4],
                               [1, 2, 3, 4],
                               [1, 2, 3, 4],
                               [1, 2, 3, 4]]


def test_begin():
    gc = GameController(800, 800)
    new_board = Board(800, 800, 100, gc)
    new_board.begin()
    assert new_board.table[3][3] == "W"
    assert new_board.table[4][4] == "W"
    gc_mini = GameController(200, 200)
    mini_board = Board(200, 200, 100, gc_mini)
    mini_board.begin()
    assert mini_board.table[0][0] == "W"
    assert mini_board.table[1][1] == "W"
    assert mini_board.table[0][1] == "B"
    assert mini_board.table[1][0] == "B"


def test_playerMove_pcMove():
    gc = GameController(40, 40)
    new_board = Board(40, 40, 10, gc)
    new_board.begin()
    new_board.playerMove(22, 35)
    assert new_board.table == [[1, 2, 3, 4],
                               [1, "W", "B", 4],
                               [1, "B", "B", 4],
                               [1, 2, "B", 4]]
    new_board.pcMove()
    assert new_board.table == [[1, 2, 3, 4],
                               [1, "W", "W", "W"],
                               [1, "B", "B", 4],
                               [1, 2, "B", 4]] or\
                              [[1, 2, 3, 4],
                               [1, "W", "B", 4],
                               [1, "W", "B", 4],
                               [1, "W", "B", 4]] or\
                              [[1, 2, 3, 4],
                               [1, "W", "B", 4],
                               [1, "B", "W", 4],
                               [1, 2, "B", "W"]]


def test_flip():
    gc = GameController(40, 40)
    new_board = Board(40, 40, 10, gc)
    new_board.table = [[1, 2, "B", 4],
                       [1, "W", "W", 4],
                       [1, "B", "B", 4],
                       [1, 2, 3, 4]]
    new_board.flip(0, 3, "B")
    assert new_board.table == [[1, 2, "B", 4],
                               [1, "W", "B", 4],
                               [1, "B", "B", 4],
                               [1, 2, 3, 4]]


def test_legalMoves():
    gc = GameController(400, 400)
    new_board = Board(400, 400, 100, gc)
    new_board.begin()
    legal_move = new_board.legalMoves("B", "W")
    assert legal_move == {(0, 1): 1, (1, 0): 1, (2, 3): 1, (3, 2): 1}


def test_on_board():
    gc = GameController(400, 400)
    new_board = Board(400, 400, 100, gc)
    assert new_board.on_board(5, 2) is False
    assert new_board.on_board(1, 3) is True


def test_tile_numbers():
    gc = GameController(400, 400)
    new_board = Board(400, 400, 100, gc)
    new_board.begin()
    new_board.table[3][2] = "B"
    new_board.tile_numbers()
    assert new_board.black == 3
    assert new_board.white == 2
