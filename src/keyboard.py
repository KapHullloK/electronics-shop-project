from src.item import Item


class Tools:

    def change_lang(self):
        if self._language == "RU":
            self._language = "EN"
        else:
            self._language = "RU"


class Keyboard(Item, Tools):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    def __repr__(self):
        return f"{Keyboard.__name__}('{self._name}', {self.price}, {self.quantity}, {self.language})"
