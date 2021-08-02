class ItemToPurchase:

    # Default constructor
    def __init__(self):
        self._item_name = "none"
        self._item_price = float(0)
        self._item_quantity = 0
        self._item_description = "none"

        # Attributes item_name, item_description, item_price, item_quantity
    def __init__(self, item_name, item_description, item_price, item_quantity):
        self._item_name = item_name
        self._item_price = item_price
        self._item_quantity = item_quantity
        self._item_description = item_description

    # Assign item_name
    def item_name(self, name):
        self._item_name = name

    # Assign item_price
    def item_price(self, price):
        self._item_price = price

    # Assign item_quantity
    def item_quantity(self, quantity):
        self._item_quantity = quantity

    # Assign item_description
    def item_description(self, description):
        self._item_description = description

    # Print item_cost with format
    def print_item_cost(self):
        total = "{:.2f}".format(self._item_quantity * self._item_price)
        print(f"{self._item_name} {self._item_quantity} @ ${self._item_price} = ${total}")

    # Print description
    def print_description(self):
        print(f"{self._item_name} : {self._item_description}")

    # Print current values before modify
    def print_modify_legend(self):
        print(f"**** Modify Item *****  ")
        print(f"Current Name: {self._item_name},")
        print(f"Current Description: {self._item_description}")
        print(f"Current Quantity: {self._item_quantity}")
        print(f"Current Price: {self._item_price}")
