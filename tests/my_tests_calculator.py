import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):  # умножение
        assert self.calc.multiply(self, 4, 3) == 12

    def test_division_correctly(self):  # деление
        assert self.calc.division(self, 6, 3) == 2

    def test_subtraction_correctly(self):  # вычитание
        assert self.calc.subtraction(self, 9, 3) == 6

    def test_adding_correctly(self):  # сложение
        assert self.calc.adding(self, 2, 3) == 5