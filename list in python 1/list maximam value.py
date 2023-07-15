
a=[1,2,3,5,4,5,6,7,8, 2, 1, 10]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)


    

    


    
