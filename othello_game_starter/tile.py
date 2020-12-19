
class Tile:
    def __init__(self, x, y):
        '''A black tile'''
        self.x = x
        self.y = y

    def display(self, color):
        '''Draws the tile'''
        if color == "B":
            fill(0)
        elif color == "W":
            fill(255)
        ellipse(self.x, self.y, 90, 90)
