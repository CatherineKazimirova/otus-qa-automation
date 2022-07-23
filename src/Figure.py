class Figure:
    def __init__(self, sides):
        self.sides = sides

    @property
    def perimeter(self):
        p = 0
        for side in self.sides:
            p += side

        return p

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Invalid argument")
        return figure.area + self.area