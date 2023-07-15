num=int(input("enter the value"))
f=1
for i in range(2,num):
    if(num%i==0):
        f=0
        break
if(f==0):
    print("not prime")
else:
    print("prime")