a = {"name": 34,"age":26,"class":40}
sum = 0
c =[]
d =[]
e = {}
for i in a:
    c.append(i)
    d.append(a[i])
for j in range(len(c)):
    for k in range(len(c)):
        if j > k:
            temp = c[j]
            c[j] = c[k]
            c[k] = temp
            print(c)




# for k,v in a.items():
#     for k1,v1 in a.items():
#         if k[0] > k1[1]:
#             temp = k[0]
#             k[0] = k1[1]
#             k1[1] = temp
            