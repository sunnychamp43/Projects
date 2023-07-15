# e = []
# for i in range(1):
#     name = (input('enter the name:-'))
#     age = int(input("enter the age:-"))
#     marks = int(input("enter the marks:-"))
#     d = {}
#     d["name"]= name
#     d["age"] = age
#     d["marks"] = marks
#     e.append(d)

# print(d)



def one (d):
    b = []
    for i in range(1):
        name = (input('enter the name:-'))
        age = int(input("enter the age:-"))
        marks = int(input("enter the marks:-"))
        d = {}
        d["name"]= name
        d["age"] = age
        d["marks"] = marks
        b.append(d)
    return b
e = one(1)
print(e)

