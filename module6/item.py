class ItemToPurchase:
    _description: object

    def __init__(self, name, description, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._description = description

    def item_name(self, name):
        self._name = name

    def item_price(self, price):
        self._price = price

    def item_quantity(self, quantity):
        self._quantity = quantity

    def item_description(self, description):
        self._description = description

    def print_item_cost(self):
        total = "{:.2f}".format(self._quantity * self._price)
        print(f"{self._name} {self._quantity} @ ${self._price} = ${total}")

    def print_description(self):
        print(f"{self._name} : {self._description}")
