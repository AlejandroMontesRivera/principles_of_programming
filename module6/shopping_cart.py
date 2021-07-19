class ShoppingCart:
    cart_items = []
    # Initialized in default constructor to "none"
    customer_name = "none"
    # Initialized in default constructor to "January 1, 2020"
    current_date = "January 1, 2020"

    # Constructor for name/date
    def __init__(self, name, date):
        self._customer_name = name
        self._current_date = date

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, cart_item):
        self.cart_items.append(cart_item)

    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name: chr):
        removed = False
        items_list = self.cart_items[:]
        for i in range(len(items_list)):
            if items_list[i]._name == item_name:
                del self.cart_items[i]
                removed = True
        if not removed:
            print("Item not found in cart. Nothing removed.")

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    def modify_item(self, modify_list):
        modify = False
        items = self.cart_items[:]
        for i in range(len(items)):
            itm = items[i]
            if itm._name == modify_list._name:
                modify = True
                # If item can be found (by name) in cart, check if parameter has default values for description,
                # price, and quantity. If not, modify item in cart.
                if modify_list._description != "none":
                    itm.item_description(modify_list._description)
                if modify_list._price != 0:
                    itm.item_price(modify_list._price)
                if modify_list._quantity != 0:
                    itm.item_quantity(modify_list._quantity)
        # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        if not modify:
            print(" ")
            print("Item not found in cart. Nothing modified.")

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        count = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            itm = items[i]
            count += itm._quantity

        return count

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        cost = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            itm = items[i]
            cost += (float(itm._quantity) * float(itm._price))
        return cost

    # Outputs total of objects in cart.
    # If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        count = len(self.cart_items)
        if count == 0:
            print("SHOPPING CART IS EMPTY")
            return 0
        print("Number of Items: " + str(count))
        for itm in self.cart_items:
            itm.print_item_cost()
        total = "{:.2f}".format(self.get_cost_of_cart())
        print(f"Total: ${total}")

    # Outputs each item's description.
    def print_descriptions(self):
        for itm in self.cart_items:
            itm.print_description()
