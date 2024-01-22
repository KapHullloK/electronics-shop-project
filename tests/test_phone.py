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


def test_3_hw4():
    phone = Phone("iPhone 14", 250, 10, 2)
    try:
        phone.number_of_sim = 0
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."


def test_4_wh4():
    phone = Phone("iPhone 14", 250, 10, 2)
    assert phone._name == "iPhone 14"
    assert phone.price == 250
    assert phone.quantity == 10
    assert phone.number_of_sim == 2
