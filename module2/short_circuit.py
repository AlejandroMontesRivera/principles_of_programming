#   Cases given for discussion
flag = False;
a = False;
b = False;


def without_return():
    flag: bool = True
    print(flag)


def with_return():
    flag: bool = True
    print(flag)
    return flag;


print("Wow >???" if without_return() and with_return() else 'Did I confuse you?');
print("Wow >???" if with_return() else 'Did I confuse you?');
print("Wow >???" if without_return() else 'Did I confuse you?');

valid1 = True
valid2 = True


def valid2() -> bool:
    valid2 = True
    return valid2


def valid1Ed() -> bool:
    valid1 = False
    return valid1

test = valid1 & valid2()

print(test)


a , b , c , d= 4, 5 , 4 ,3

# CASE A
if a < b:
    if c > d:
        print('Looking good')
else:
    print('Looking wrong')

# CASE B
if a < b & c > d:
    print('Looking good')
else:
    print('Looking wrong')

# CASE C
if a < b and c > d:
    print('Looking good')
else:
    print('Looking wrong')


a, b = 25, 4
print(a & b)
print(a and b)

a , b , c , d= 4, 5 , 4 ,3
# CASE A
if a < b:
    if c > d:
        print('Looking good')
else:
    print('Looking wrong')
# CASE B
if a < b & c > d:
    print('Looking good')
else:
    print('Looking wrong')
# CASE C
if a < b and c > d:
    print('Looking good')
else:
    print('Looking wrong')