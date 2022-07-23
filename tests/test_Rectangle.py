from src.Rectangle import Rectangle


def test_rectangle():
    rectangle = Rectangle(3, 8)
    assert rectangle.name == "Rectangle"
    assert rectangle.area == 24
    assert rectangle.perimeter == 22




