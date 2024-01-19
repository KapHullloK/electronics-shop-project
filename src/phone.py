from src.item import Item


class Phone(Item):
    def __init__(self, _name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(_name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other) -> int | None:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    def __repr__(self):
        return f"{Phone.__name__}('{self._name}', {self.price}, {self.quantity}, {self.number_of_sim})"
