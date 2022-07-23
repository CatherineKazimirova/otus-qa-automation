from src.Square import Square


def test_square():
    square = Square(10)
    assert square.name == "Square"
    assert square.area == 100
    assert square.perimeter == 40
