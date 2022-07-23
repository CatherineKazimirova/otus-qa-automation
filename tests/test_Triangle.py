from src.Triangle import Triangle
import pytest


def test_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.name == "Triangle"
    assert triangle.area == 6
    assert triangle.perimeter == 12


def test_value_error():
    with pytest.raises(ValueError) as error_info:
        Triangle(2, 1, 3)

    assert str(error_info.value) == "Invalid arguments"

    with pytest.raises(ValueError) as error_info:
        Triangle(1, 1, 3)

    assert str(error_info.value) == "Invalid arguments"



