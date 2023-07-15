num = int(input('enter the value:'))
digit = num
rev = 0

while digit > 0:
    temp = digit % 10
    rev = rev * 10 + temp
    digit = digit //10
# if num == rev:
#     print('Palidrome no')
# else:
#     print('Not Palidrome no')
print(rev)