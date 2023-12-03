# a class called Pawn that inherits from Piece
from piece import Piece
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Pawn", position)
    def move(self, new_position):
        super().move(new_position)