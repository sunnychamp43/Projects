a=int(input("enter the odd value"))
b=int(input("enter the even value"))
evensum=0
oddsum=0
for i in range(a+1):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print(evensum)
print(oddsum)    