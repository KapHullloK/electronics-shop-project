import pytest

from src.keyboard import Keyboard

keyb1 = Keyboard('Dark Project KD87A', 9600, 5)
keyb2 = Keyboard('HyperX Alloy Core', 7600, 10)


def test_1_hw5():
    assert keyb1._name == "Dark Project KD87A"
    assert keyb1.price == 9600
    assert keyb1.quantity == 5
    assert keyb1.language == "EN"


def test_2_hw5():
    print(repr(keyb1))
    assert repr(keyb1) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_3_hw5():
    try:
        keyb2.language = "UK"
    except AttributeError as e:
        assert str(e) == "property 'language' of 'Keyboard' object has no setter"
