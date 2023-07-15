# a = [1,2,3,4,5,6,7,8]
# b =[]
# for i in range(0,len(a),2):
#     c=[]
#     for j in range(i,i+2):
            
                  
#         c.append(a[j])
#     b.append(c)
# print(b)
    
# a= int(input( ''))
# b = int (input(" "))
# for i in range(a,b):
#     if (i%2==0):
#         print(i)
#     else:
#         print(i)

def mlist (a):
    b = []
    for i in range(0,len(a),2):
        c = []
        for j in range(i,i+2):
            c.append(a[j])
        b.append(c)
    return b
print(mlist ([1,2,3,4,5,6,7,8]))



