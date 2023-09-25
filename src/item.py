import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @property
    def return_name(self):
        return self._name

    @return_name.setter
    def return_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name[0:11]

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, encoding="cp1251") as CSVfile:
            read = csv.DictReader(CSVfile)
            for row in read:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        return int(string.split('.')[0])


if __name__ == '__main__':
    Item.instantiate_from_csv("items.csv")
    print(Item.all[4].quantity)
