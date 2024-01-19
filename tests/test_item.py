import pytest

from src.item import Item
from src.phone import Phone


def test_1_hw1():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_2_hw1():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.8
    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 16000.0
    assert item1.quantity == 20
    assert item2.quantity == 5


def test_3_hw2():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.set_name == "Смартфон"

    item1.set_name = "Планшет"
    assert item1.set_name == "Планшет"

    Item.all.clear()
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[3].price == 50.0
    assert Item.all[4].quantity == 5


def test_4_hw2():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('2340.567') == 2340


def test_5_hw3():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"
    assert str(item2) == 'Ноутбук'


def test_6_hw4():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    phone1 = Phone("iPhone 14", 120_000, 5, 1)
    phone2 = Phone("iPhone 14", 100_000, 7, 2)

    assert phone1 + item1 == 25
    assert phone2 + item2 == 12
