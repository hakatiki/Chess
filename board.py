from piece import *
class Board():
    def __init__(self):
        self.starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

        self.starting_matrix = ""
        for i in self.starting_position:
            if i == '/':
                continue
            elif i == '8':
                self.starting_matrix += 'xxxxxxxx'
            else:
                self.starting_matrix += i
        self.turn = 'white'
        self.current_matrix = self.starting_matrix
    def get_xy(self, x, y):
        if isinstance(x,str):
            x = int(ord(x) - ord('a') + 1)
        return self.current_matrix[(8-y)*8+x-1]