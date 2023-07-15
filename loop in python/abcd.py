a=int(input("enter the value"))
b=64
for i in range(1,a+1):
    b=b+1
    print(chr(b))
    for j in range(i):
        b=b+1
        print(chr(b),end="")
