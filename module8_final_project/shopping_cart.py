from item_to_purchase import ItemToPurchase


class ShoppingCart:

    # Default
    def __init__(self):
        # Initialized in default constructor to "none"
        self._customer_name = "none"
        # Initialized in default constructor to "January 1, 2020"
        self._current_date = "January 1, 2020"
        self._cart_items = []

    # Constructor for name/date
    def __init__(self, customer_name, current_date):
        self._customer_name = customer_name
        self._current_date = current_date
        self._cart_items = []

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, cart_item):
        self._cart_items.append(cart_item)

    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name: chr):
        removed = False
        items_list = self._cart_items[:]
        for i in range(len(items_list)):
            if items_list[i]._item_name == item_name:
                del self._cart_items[i]
                removed = True
        if not removed:
            print("Item not found in cart. Nothing removed.")

    # Modifies an item's description, price, and/or quantity.
    def modify_item(self, itm_index):
        if itm_index >= 0:
            item = self._cart_items[itm_index]
            item.print_modify_legend()
            item_name = input("Enter new name: ")
            item_desc = input("Enter new description: ")
            item_price = float(input("Enter new price: "))
            item_qty = int(input("Enter new quantity: "))
            self._cart_items[itm_index] = ItemToPurchase(item_name, item_desc, item_price, item_qty)
        else:
            print('Item not found in cart. Nothing modified.')

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        count = 0
        items = self._cart_items[:]
        for i in range(len(items)):
            itm = items[i]
            count += itm._item_quantity

        return count

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        cost = 0
        items = self._cart_items[:]
        for i in range(len(items)):
            itm = items[i]
            cost += (float(itm._item_quantity) * float(itm._item_price))
        return cost

    # Outputs total of objects in cart.
    # If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        count = len(self._cart_items)
        if count == 0:
            print("SHOPPING CART IS EMPTY")
            return 0
        print("Number of Items: " + str(self.get_num_items_in_cart()))
        for itm in self._cart_items:
            itm.print_item_cost()
        total = "{:.2f}".format(self.get_cost_of_cart())
        print(f"Total: ${total}")

    # Outputs each item's description.
    def print_descriptions(self):
        print("Item Descriptions")
        for itm in self._cart_items:
            itm.print_description()

    # Retrieves item by name
    def get_item_by_name(self, item_name) -> int:
        items = self._cart_items[:]
        pos = -1
        for i in range(len(items)):
            itm = items[i]
            if itm._item_name == item_name:
                pos = i
                break
        return pos
