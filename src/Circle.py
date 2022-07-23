from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, side):
        super(Circle, self).__init__([side])
        self.side = side

    @property
    def name(self):
        return "Circle"

    @property
    def area(self):
        return round((self.side ** 2) / (4 * math.pi))
