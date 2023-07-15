
# a=[1,2,2,2,4,3,4,5,4]
# b=[]
# c =0
# d = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         c = a.count(i)
#         d.append(c)
# print(b)
# print(d)




# 2nd method of count value 

a=[1,2,2,2,4,3,4,5,4,6,6,6,6,6]
b=[]
c = []

sum = 0

for i in a:
    
    if i not in b:
        count = 0
        b.append(i)

        for j in a:
            
            if j == i:
                count +=1
        c.append(count)
print(b)
print(c)
