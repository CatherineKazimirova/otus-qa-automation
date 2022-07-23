from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super(Square, self).__init__([side, side, side, side])
        self.side = side

    @property
    def name(self):
        return "Square"

    @property
    def area(self):
        return self.side * self.side
