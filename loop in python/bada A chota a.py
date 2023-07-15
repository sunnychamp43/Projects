b=str(input("enter the value"))
c=ord(b)
d=0
if(c<97):
    d=c+32
    print(chr(d))
elif(c>96):
    d=c-32
    print(chr(d))
a