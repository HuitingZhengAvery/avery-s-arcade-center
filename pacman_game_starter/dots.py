from dot import Dot


class Dots:
    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    def eat(self, x, y):
        """Eat dots when they are within Pacman's eat distance"""
        for i in self.top_row:
            if x > self.WIDTH - self.EAT_DIST:
                if i.x == 0 and abs(i.y - y) < self.EAT_DIST:
                    del self.top_row[self.top_row.index(i)]
            if x < self.EAT_DIST:
                if i.x == self.WIDTH and abs(i.y - y) < self.EAT_DIST:
                    del self.top_row[self.top_row.index(i)]
            if abs(i.x - x) < self.EAT_DIST and abs(i.y - y) <\
               self.EAT_DIST:
                del self.top_row[self.top_row.index(i)]
        for j in self.left_col:
            if y > self.HEIGHT - self.EAT_DIST:
                if j.y == 0 and abs(j.x - x) < self.EAT_DIST:
                    del self.left_col[self.left_col.index(j)]
            if y < self.EAT_DIST:
                if j.y == self.HEIGHT and abs(j.x - x) < self.EAT_DIST:
                    del self.left_col[self.left_col.index(j)]
            if abs(j.x - x) < self.EAT_DIST and abs(j.y - y) < self.EAT_DIST:
                del self.left_col[self.left_col.index(j)]
        for k in self.bottom_row:
            if x > self.WIDTH - self.EAT_DIST:
                if k.x == 0 and abs(k.y - y) < self.EAT_DIST:
                    del self.bottom_row[self.bottom_row.index(k)]
            if x < self.EAT_DIST:
                if k.x == self.WIDTH and abs(k.y - y) < self.EAT_DIST:
                    del self.bottom_row[self.bottom_row.index(k)]
            if abs(x - k.x) <= self.EAT_DIST and abs(k.y - y) < self.EAT_DIST:
                del self.bottom_row[self.bottom_row.index(k)]
        for p in self.right_col:
            if y > self.HEIGHT - self.EAT_DIST:
                if p.y == 0 and abs(p.x - x) < self.EAT_DIST:
                    del self.right_col[self.right_col.index(p)]
            if y < self.EAT_DIST:
                if p.y == self.HEIGHT and abs(p.x - x) < self.EAT_DIST:
                    del self.right_col[self.right_col.index(p)]
            if abs(p.x - x) < self.EAT_DIST and abs(p.y - y) < self.EAT_DIST:
                del self.right_col[self.right_col.index(p)]

    def dots_left(self):
        """Returns the number of remaing dots in the c  ollection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))
