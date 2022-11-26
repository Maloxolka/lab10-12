line = [0] * 9
board = []
for i in range(9):
    board.append(line.copy())


class Sudoku:
    def __init__(self):
        self.board = board.copy()

    def print_board(self):
        for j in range(9):
            print(self.board[j])

    def check_line(self, x, value):
        return self.board[x].count(value) == 0

    def check_column(self, y, value):
        column = []
        for j in range(9):
            column.append(self.board[j][y])
        return column.count(value) == 0

    def check_square(self, x, y, value):
        square = []
        x_range = []
        y_range = []
        if x in range(3):
            x_range = range(3)
        if x in range(3, 6):
            x_range = range(3, 6)
        if x in range(6, 9):
            x_range = range(6, 9)
        if y in range(3):
            y_range = range(3)
        if y in range(3, 6):
            y_range = range(3, 6)
        if y in range(6, 9):
            y_range = range(6, 9)
        for j in x_range:
            for k in y_range:
                square.append(self.board[j][k])
        return square.count(value) == 0

    def place(self, x, y, value):
        if self.check_line(x, value) and self.check_column(y, value) and self.check_square(x, y, value):
            self.board[x][y] = value
            print("+")
        else:
            print("-")
