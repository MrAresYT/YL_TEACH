class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return self.__class__.__name__[0]


class Queen(Pawn):
    pass


pie = Queen(1, 1, 1)
print(pie.char())
