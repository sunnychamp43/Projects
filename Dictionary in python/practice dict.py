# d = {"name":"ajay","age":30,"street":10,"city":"delhi"}
# # d.pop("city")
# # d.update({"state": "delhi"})
# # for k,v in d.items():
#     # print(k)
#     # print(v)
# d["zone"] = "kolkata"
# print(d)
    


a = [1,2,3,4,5]
b= {}


# b = {i : i*i for i in a}
for i in range(len(a)):
    b[a[i]] = a[i] * a[i]
print(b)    
    
    