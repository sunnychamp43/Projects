
a = int(input("enter the value:"))
b = int(input("enter the value:"))
sum =0
for i in range(a,b+1):
    if i%2==0:
        sum= sum-i
    else:
        sum=sum+i
    print(sum)


    