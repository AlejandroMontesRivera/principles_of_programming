is_leap_year = False
input_year = int(input())
century = input_year % 100 == 0
var = 'not a'
if century and input_year % 400 == 0:
    var = ''
elif not century and input_year % 4 == 0:
    var = ''
print(f"{input_year} - {var}leap year")
