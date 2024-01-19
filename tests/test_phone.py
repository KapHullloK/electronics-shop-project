import pytest

from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 1)
phone2 = Phone("iPhone 13", 100_000, 7, 2)


def test_1_hw4():
    assert phone1.number_of_sim == 1
    assert phone2.number_of_sim == 2


def test_2_hw4():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 1)"
    assert repr(phone2) == "Phone('iPhone 13', 100000, 7, 2)"
