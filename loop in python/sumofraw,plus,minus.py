a=int(input("enter the value"))
b=int(input("enter the value"))
for i in range(a,b):
    if(i%2==0):
        print(i,end="+")
    else:
        print(i,end="-")