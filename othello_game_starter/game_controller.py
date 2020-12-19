import time


class GameController:
    '''Maintains the state of the game.'''
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FILE_NAME = "scores.txt"
        self.black_wins = False
        self.white_wins = False
        self.game_ends = False
        self.tie = False
        self.player_name = False
        self.num = 0
        self.black = 0

    def update(self):
        '''Prints the game result to the screen'''
        if self.game_ends:
            fill(222, 49, 99)
            textSize(40)
            textAlign(CENTER)
            if self.tie:
                result = 'Tie game, each player has ' +\
                         str(self.num) + ' tiles'
                text(result, self.WIDTH / 2, self.HEIGHT / 2)
            else:
                result = "Winner has " + str(self.num) + " tiles"
                if self.black_wins:
                    text("You won!", self.WIDTH / 2,
                         self.HEIGHT / 2 - 100)
                    text(result, self.WIDTH / 2, self.HEIGHT / 2)
                elif self.white_wins:
                    text("Computer won", self.WIDTH / 2,
                         self.HEIGHT / 2 - 100)
                    text(result, self.WIDTH / 2, self.HEIGHT / 2)
            if self.player_name is False:
                name = self.input('Enter your name')
                if name:
                    print('Hi, ' + name)
                elif name == '':
                    print('[empty string]')
                else:
                    print(name)  # Canceled dialog will print None
                self.score(name, self.black)
                self.player_name = True

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def score(self, name, score):
        fhand = open(self.FILE_NAME, 'r')
        scores = []
        for line in fhand:
            scores.append(line)
        if name:
            new_score = name + " " + str(score) + '\n'
        else:
            new_score = "Anonymous " + str(score) + '\n'
        scores.append(new_score)

        fhand = open(self.FILE_NAME, 'w')
        for line in scores:
            fhand.write(line)
