a=int(input("enter the value"))
sum=0
for i in range(0,a):
    c=i+1
    print(end="(")
    for num in range(c):
        c=num+1
        print(c,end="")
        for j in range(c):
            if(c%2==0):
                sum=sum-c
            else:
                sum=sum+c
        print(end="+")
    if(i%2==0):
        print(end="\b)-")
    else:
        print(end="\b)+")
print(end="\b=")
print(sum,end="")