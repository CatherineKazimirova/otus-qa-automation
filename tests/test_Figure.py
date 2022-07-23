from src.Figure import Figure
import pytest


class Dummy(Figure):
    def __init__(self, area):
        self.area = area


def test_add_area():
    dummy1 = Dummy(10)
    dummy2 = Dummy(15)
    total_area = dummy1.add_area(dummy2)
    assert total_area == 25


def test_value_error():
    dummy = Dummy(10)
    with pytest.raises(ValueError) as error_info:
        dummy.add_area(123)

    assert str(error_info.value) == "Invalid argument"



