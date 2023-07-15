a=int(input("enter the starting no"))
b=int(input("enter the ending no"))
for i in range(a,b):
        f = 1
        for num in range(2,i):
            if(i%num==0):
                f = 0
                break
        if f==1:
            print(i)
