import csv
import os


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{Item.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self._name}"

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @property
    def set_name(self):
        return self._name

    @set_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name[0:11]

    @classmethod
    def instantiate_from_csv(cls, path=""):
        try:
            f = CheckCSV(path)
        except FileNotFoundError as e:
            raise e
        except InstantiateCSVError as e:
            raise e

        with open(path, encoding="cp1251") as CSVfile:
            read = csv.DictReader(CSVfile)
            for row in read:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        return int(string.split('.')[0])

    def __add__(self, other) -> int | None:
        if isinstance(other, Item) or issubclass(other.__class__, Item):
            return self.quantity + other.quantity
        return None


class InstantiateCSVError(Exception):
    def __str__(self):
        return "Файл item.csv поврежден"


class CheckCSV:
    def __init__(self, f_path: str):
        if not os.path.exists(f_path):
            raise FileNotFoundError("Отсутствует файл item.csv")

        with open(f_path) as CSVfile:
            read = csv.reader(CSVfile)
            first_row = next(read, None)
            if first_row is not None:
                for i in read:
                    if len(first_row) != len(i):
                        raise InstantiateCSVError
            else:
                raise InstantiateCSVError
