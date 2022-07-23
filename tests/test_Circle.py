from src.Circle import Circle


def test_circle():
    circle = Circle(10)
    assert circle.name == "Circle"
    assert circle.area == 8
    assert circle.perimeter == 10
