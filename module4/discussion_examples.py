import random;

# Loop for a list of countries
food = {"MEXICO": "TACOS", "USA": "BURGERS", "JAPAN": "SUSHI"}
# for food, country in food.items():
#    print(f'{food}, belongs to  ,{country}')

# x = 0
# y = 5
# while x != y:
#    print(x)   #Print number
#     x = random.randint(0,10)  #pick a new number

food = {"MEXICO": "TACOS", "USA": "BURGERS", "JAPAN": "SUSHI"}
list(map(lambda x: print(food), 'test'))

# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
print(list(map(lambda i: i + i, numbers)))

a = int(input())
checker = False

a = int(input())
checker = True

while checker:
    if 20 <= a <= 98:
        tmpA = str(a)
        checker = (tmpA[0] != tmpA[0])
        a -= 1
        print(a)
