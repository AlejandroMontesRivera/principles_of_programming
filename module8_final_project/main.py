from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart


# Menu function
def print_menu(cart):
    print("*********** MENU **************")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


# Name and Date entered
name = input("Enter the customer's name: ")
date = input("Enter date: ")

# Output the name and date.
print(f"Customer name: {name}")
print(f"Today's date: {date}")

# Create an object of type ShoppingCart
shopping_cart = ShoppingCart(name, date)
# Logic to handle the option
opt = ""
while opt != "q":
    print_menu(shopping_cart)
    opt = input("Choose an option: ").lower().strip()
    # Hint: Implement Quit before implementing other options.
    if opt == "q":
        break;
    elif opt == "a":
        print("**** ADD ITEM ****")
        item_name = input("Name: ")
        item_desc = input("Description: ")
        item_price = float(input("Price: "))
        item_qty = int(input("Quantity: "))
        shopping_cart.add_item(ItemToPurchase(item_name, item_desc, item_price, item_qty))
    elif opt == "r":
        print("**** REMOVE ITEM FROM CART ****")
        item_name = input("Enter the name of item to remove: ")
        shopping_cart.remove_item(item_name)
    elif opt == "c":
        print("**** CHANGE ITEM QUANTITY *****")
        item_name = input("Name: ")
        # Modify Item by Name
        shopping_cart.modify_item(int(shopping_cart.get_item_by_name(item_name)))

    elif opt == "i":
        print("**** OUTPUT ITEMS' DESCRIPTIONS ****")
        print(f"{name}'s Shopping Cart - {date}")
        shopping_cart.print_descriptions()
    elif opt == "o":
        print('**** OUTPUT SHOPPING CART **** ')
        print(f"{name}'s Shopping Cart - {date}")
        shopping_cart.print_total()
