#  Option #1: Retail Total
#  A customer in a store is purchasing five retail items.
#  Write a program that asks for the price of each item and then displays the subtotal of the sale,
#  the amount of sales tax, and the total. Assume the sales tax is 7 percent.

def get_total():
    return sum(priceList)


def calculate_tax(qty, total):
    return qty * float(1.07) if total else qty * float(.07)


def format_dec(num):
    return "{:.2f}".format(num)


while True:
    try:
        print("Welcome to **WE LIVE IN A SIMULATION** store");

        items = int(input('How many items are you buying today?: '))
        priceList = []
        while items != 0:
            price = float(input("Enter the price of the item {} : ".format(items)))
            priceList.append(price)
            print("Price with tax : ${}".format(format_dec(calculate_tax(price, True))))
            items -= 1

        print("********************************************************")
        print("Your subtotal is ${}".format(format_dec(get_total())))
        print("Your sale tax is ${}".format(format_dec(calculate_tax(get_total(), False))))
        print("Your total total is ${}".format(format_dec(calculate_tax(get_total(), True))))
        print("********************************************************")

        print("Thank you for coming to **WE LIVE IN A SIMULATION** store");
        input("Press Enter to continue...")

    except ValueError:
        print("Only numbers are accepted inputs.")
