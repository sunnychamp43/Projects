name = "piyush sharma"
output = ""
for nm in name.split(" "):
    print(nm[0].upper())
    print("{}{}".format(nm[0].upper(),nm[1:]))
    output+= "{}{} ".format(nm[0].upper(),nm[1:])
    print(output)


# n = 5
# for i in range(1,11):
    # a = n*i
    # print(a)
    # print("{} X {} = {}".format(n,i,a))
    # print(f"{n} X {i} = {a}")