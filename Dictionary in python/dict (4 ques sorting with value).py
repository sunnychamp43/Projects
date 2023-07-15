
a = {"marks":26,"pincode":33,"age":12,"Class":9,"id":20}
c = []
d = []
for k,v in a.items():
    for k1,v1 in a.items():

        if a[k]  < a[k1]:
            temp = a[k] 
            a[k] = a[k1] 
            a[k1] = temp
print(a)

            
    
    
    

