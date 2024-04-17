class Figure:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return self.__class__.__name__[0]

    def get_color(self):
        return self.color


class Knight(Figure):
    def can_move(self, row1, col1):
        n = row1 + col1 - self.col + self.row
        if abs(n) == 3:
            return True
        else:
            return False



WHITE = 1
BLACK = 2

row0 = 2
col0 = 2
knight = Knight(row0, col0, WHITE)

print('white' if knight.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(knight.char(), end='')
        elif knight.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
