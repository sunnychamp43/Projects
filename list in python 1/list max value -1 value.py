# range ke through
# a = [1,3,7,31,19,21,16,27,18,24]
# b = a[0]
# c= a[0]
# for i in range(0,len(a)):
#     if a[i] > b:
#          b = a[i]
         
# for j in range(0,len(a)):  
#     if a[j] > c and a[j] != b :
#         c = a[j] 
# print(c)


# list ke throught
# a = [1,3,7,31,19,21,16,27,18,24]
# b = a[0]
# c= a[0]
# for i in a:
#     if i > b:
#         b = i 
# for j in a:
#     if j > c and j != b :
#         c = j 
# print(c)



def max2 (a):
    b = a[0]
    c = a[0]
    for i in a:
        if i > b:
            b = i
    for j in a:
        if j > c and j != b:
            c = j
    return c
print(max2 ([1,2,34,23,65,78,26]))

            
        
            

    







# a = [9,7,1,3,21,8,10]
# b=a[0]
# for i in a:
#     if i > b:
#         b=i
# print(b)
