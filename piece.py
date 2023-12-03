# a class called piece that holds information about a chess piece
class Piece():
    def __init__(self, color, name, position):
        self.color = color
        self.name = name
        self.position = position
        self.moved = False
    def __str__(self):
        return self.color + " " + self.name + " at " + self.position
    def __repr__(self):
        return self.color + " " + self.name + " at " + self.position
    def move(self, new_position):
        self.position = new_position
        self.moved = True