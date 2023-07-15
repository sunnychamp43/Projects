dig = int(input('enter the value'))
value = dig

rev = 0

while value > 0:
    rem = value % 10
    rev = rev * 10 + rem
    value = value // 10
print('reverse',rev)