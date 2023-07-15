a=int(input('enter the even value'))
b=int(input('enter the even value'))
sum=0
for i in range(a,b+1):
    if(i%2==0):
        sum=sum+1
    else:
        sum=sum-1
print(sum)