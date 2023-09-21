import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_1_that_needs_resource():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_2_that_does_not():
    Item.pay_rate = 0.8
    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 16000.0

