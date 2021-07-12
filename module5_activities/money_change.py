# Dollars, Quarters, Dimes, Nickels, and Pennies.
change = int(input())
dollars = (change - (change % 100)) / 100
if dollars > 0:
    print(f"{dollars} {'Dollars' if (dollars > 1) else 'Dollar'}")
    change -= dollars * 100
quarters = (change - (change % 25)) / 25
if quarters > 0:
    print(f"{quarters} {'Quarters' if (quarters > 1) else 'Quarter'}")
    change -= quarters * 25
dimes = (change - (change % 10)) / 10
if dimes > 0:
    print(f"{dimes} {'Dimes' if (dimes > 1) else 'Dime'}")
    change -= dimes * 10
nickels = (change - (change % 5)) / 5
if nickels > 0:
    print(f"{nickels} {'Nickels' if (dimes > 1) else 'Nickel'}")
    change -= nickels * 5
pennies = (change - (change % 1))
if pennies > 0:
    print(f"{pennies} {'Pennies' if (dimes > 1) else 'Penny'}")
