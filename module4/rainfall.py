# Adding calendar library to retrieve the month name
import calendar
# Ask the user for the number of years
try:
    num_years = int(input("Enter the number of years: "))
except ValueError:
    print("That's not an int")
num_months = num_years * 12
# Total inches summary variable
total_inches = 0
# Outer loop to iterate over years
for years in range (0, num_years):
    print(f"Year {years + 1}")
    # Inner loop to iterate over months
    for month_idx in range(1, 13):
        # Retrieve month name using calendar.month_name
        month = calendar.month_name[month_idx]
        # Assign the inches of rainfall per month
        try:
            inches_rainfall = int(input(f"Enter the inches of rainfall in {month}: "))
        except ValueError:
            print("That's not an int")
        # Retrieve total
        total_inches += inches_rainfall
print(f"**** Number of months : {num_months}")
print(f"**** The total inches of rainfall in {num_years}  years was: {total_inches}")
print(f"**** The average rainfall per month was: {total_inches / num_months}")
