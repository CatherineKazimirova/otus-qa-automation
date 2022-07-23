from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a_side, b_side):
        super(Rectangle, self).__init__([a_side, b_side, a_side, b_side])
        self.a_side = a_side
        self.b_side = b_side

    @property
    def name(self):
        return "Rectangle"

    @property
    def area(self):
        return self.a_side * self.b_side



