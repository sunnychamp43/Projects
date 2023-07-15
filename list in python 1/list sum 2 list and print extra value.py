a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,4,5,7]
sum = 0
c = []

d = len(a)
e = len(b)

if len(a) > len(b):
    for i in range(len(a)):
        # if len(a) > len(b) :

        b.append(0)        
        sum = a[i] + b[i]
        c.append(sum)
    print(c)

elif len(b) > len(a):   
    for i in range(len(b)):
        # if len(b) > len(a) :
        a.append(0)        
        sum = a[i] + b[i]
        c.append(sum)
    print(c)


    
    
    
    

    
    
    
        
    
        
          

