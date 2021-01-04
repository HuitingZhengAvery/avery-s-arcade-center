from game_board import Board
from game_controller import GameController

WIDTH = 800
HEIGHT = 800
GRID = 100

game_controller = GameController(WIDTH, HEIGHT)
game_board = Board(WIDTH, HEIGHT, GRID, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    background(34, 139, 34)
    strokeWeight(2)
    for i in range(1, HEIGHT // GRID):
        line(0, i * GRID, WIDTH, i * GRID)
        line(i * GRID, 0, i * GRID, HEIGHT)
    game_board.begin()
    

def draw():
    game_board.update()
    game_controller.update()


def mousePressed():
    if game_controller.game_ends is False and game_board.whiteTurn is False:
        game_board.playerMove(mouseX, mouseY)
