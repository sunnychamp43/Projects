a
b=str(input("enter the value"))
c=ord(b)

if(c>96):
    c=c-32

elif(c>64):
    c=c+32


if(c<64):
    print('invalid')

elif(c>122):
    print('invalid')

elif(c>90 and c<95):
    print('invalid')
else:
    print(chr(c))    