from dots import Dots


class Maze:
    """Draws the maze and handles interaction between Pacman and dots"""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ,
                 game_controller):
        self.LEFT_VERT = LEFT_VERT
        self.RIGHT_VERT = RIGHT_VERT
        self.TOP_HORIZ = TOP_HORIZ
        self.BOTTOM_HORIZ = BOTTOM_HORIZ
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.gc = game_controller
        self.dots = Dots(WIDTH, HEIGHT,
                         LEFT_VERT, RIGHT_VERT,
                         TOP_HORIZ, BOTTOM_HORIZ)

    def eat_dots(self, x_pac, y_pac):
        """Pass Pacman's location to eat method in Dots"""
        self.dots.eat(x_pac, y_pac)

    def update(self):
        """Make necessary per-frame updates"""
        # Check whether the dots are all eaten
        if self.dots.dots_left() == 0:
            self.gc.player_wins = True

    def display(self):
        """Display the maze"""
        self.update()

        # Display the dots
        self.dots.display()

        # Draw the maze walls
        stroke(0.0, 0.0, 10)
        strokeWeight(5)
        fill(0)
        rectMode(CORNER)

        clearance = 60
        overdraw = 20  # Start drawing offscreen
        t = -(overdraw)
        left = -(overdraw)
        border = 20
        big_rad = 30
        small_rad = 17

        # Upper left
        t = -(overdraw)
        left = -(overdraw)
        w = self.LEFT_VERT - clearance + overdraw
        h = self.TOP_HORIZ - clearance + overdraw
        rect(left, t, w, h, big_rad)
        rect(left, t, w - border, h - border, small_rad)

        # Upper middle
        t = -(overdraw)
        left = self.LEFT_VERT + clearance
        w = (self.RIGHT_VERT - clearance) - (self.LEFT_VERT + clearance)
        rect(left, t, w, h, big_rad)
        rect(left + border, t, w - border*2, h - border, small_rad)

        # Upper right
        left = self.RIGHT_VERT + clearance
        w = self.RIGHT_VERT - clearance + overdraw
        rect(left, t, w, h, big_rad)
        rect(left + border, t, w - border*2, h - border, small_rad)

        # Middle left
        t = self.TOP_HORIZ + clearance
        left = -(overdraw)
        w = self.LEFT_VERT - clearance + overdraw
        h = (self.BOTTOM_HORIZ - clearance) - (self.TOP_HORIZ + clearance)
        rect(left, t, w, h, big_rad)
        rect(left, t + border, w - border, h - border*2, small_rad)

        # Middle middle
        left = self.LEFT_VERT + clearance
        t = self.TOP_HORIZ + clearance
        w = (self.RIGHT_VERT - clearance) - (self.LEFT_VERT + clearance)
        rect(left, t, w, h, big_rad)
        rect(left + border, t + border, w - border*2, h - border*2, small_rad)

        # Middle right
        left = self.RIGHT_VERT + clearance
        t = self.TOP_HORIZ + clearance
        w = self.RIGHT_VERT - clearance + overdraw
        rect(left, t, w, h, big_rad)
        rect(left + border, t + border, w - border*2, h - border*2, small_rad)

        # Lower left
        w = self.LEFT_VERT - clearance + overdraw
        h = self.TOP_HORIZ - clearance + overdraw
        left = -(overdraw)
        t = self.BOTTOM_HORIZ + clearance
        rect(left, t, w, h, big_rad)
        rect(left, t + border, w - border, h - border, small_rad)

        # Lower middle
        left = self.LEFT_VERT + clearance
        w = (self.RIGHT_VERT - clearance) - (self.LEFT_VERT + clearance)
        rect(left, t, w, h, big_rad)
        rect(left + border, t + border, w - border*2, h - border, small_rad)

        # Lower right
        left = self.RIGHT_VERT + clearance
        w = self.RIGHT_VERT - clearance + overdraw
        rect(left, t, w, h, big_rad)
        rect(left + border, t + border, w - border*2, h - border, small_rad)
