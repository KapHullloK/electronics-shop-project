import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_1_hw1():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_2_hw1():
    Item.pay_rate = 0.8
    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 16000.0
    assert item1.quantity == 20
    assert item2.quantity == 5


def test_3_hw2():
    assert item1.return_name == "Смартфон"

    item1.return_name = "Планшет"
    assert item1.return_name == "Планшет"

    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 7
    assert Item.all[5].price == 50.0
    assert Item.all[6].quantity == 5


def test_4_hw2():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('2340.567') == 2340
