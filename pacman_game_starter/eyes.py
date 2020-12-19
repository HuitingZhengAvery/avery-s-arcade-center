from eye import Eye


class Eyes:
    def __init__(self):
        self.left_eye = Eye()
        self.right_eye = Eye()

    def display(self, x, y, direction):
        self.left_eye.look(direction)
        self.right_eye.look(direction)
        self.left_eye.display(x-20, y)
        self.right_eye.display(x+20, y)
