from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a_side, b_side, c_side):
        super(Triangle, self).__init__([a_side, b_side, c_side])
        self._validate_sides(a_side, b_side, c_side)
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def _validate_sides(self, a_side, b_side, c_side):
        cond1 = a_side + b_side <= c_side
        cond2 = a_side + c_side <= b_side
        cond3 = b_side + c_side <= a_side

        if cond1 or cond2 or cond3:
            raise ValueError("Invalid arguments")

    @property
    def name(self):
        return "Triangle"

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)) ** 0.5



