from tile import Tile


class Tiles:
    def __init__(self, GRID, table):
        self.GRID = GRID
        self.centre = self.GRID // 2
        self.table = table

    def display(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j] == "B":
                    Tile(j * self.GRID + self.centre, i *
                         self.GRID + self.centre).display("B")
                elif self.table[i][j] == "W":
                    Tile(j * self.GRID + self.centre, i *
                         self.GRID + self.centre).display("W")
