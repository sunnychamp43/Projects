# 2 star tree reverse and straight 

a = int(input("enter the star:"))
for num in range(a,0,-1):
    for l in range(1,18-num,1):
        print(" ",end="")
    for m in range(num):
        print("*",end=" ")
    print(" ")

for i in range(1,a-1):
    for j in range(1,17-i):
        print(" ",end="")
    for k in range(1*i+1):
        print("*",end=" ")
    print(" ")

# star X pattern 

# a = int(input("Enter the X star = "))


# for i in range(0, a):
#     for j in range(0, a):
#         if (i==j or j==a -1 -i):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print(" ")



# 2nd star X pattern 



# a = int(input("Enter the X star = "))
# sum= 0


# for i in range(0, a):

    
#     for j in range(0, a):

#         if (i==j or j==a -1 -i):
#             print("*",end="")
        
#         elif i==0:
#             print("*",end="")
    
#         elif i==a-1:
#             print("*",end="")

#         # elif j==0:
#             # print("*",end="")
#         else:
            
            
#             print(" ",end="")
#     print("  ")




# # 4th star pattern 

# a = int(input("Enter the X star = "))
# sum= 0


# for i in range(0, a):

    
#     for j in range(0, a):

#         if (i==j or j==a -1 -i):
#             print("*",end="")
        
#         elif j==0:
#             print("*",end="")
#         else:
            
#             print(" ",end="")
#     print("*",end="")
        
#     print("  ")
