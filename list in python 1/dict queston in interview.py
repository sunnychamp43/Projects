# sort the names in list based in second last index 
l = ['vijay',"pankaj","rahul","viney","mamta"]
sorted(l,key = lambda s : s[-2])


# 2. sort list of dictonary based on specific key 

from operator import itemgetter
d = [{"name":"ram","age":14,"marks":56,},{"name":"radha","age":11,"marks":69}]
sorted(d, key=itemgetter("age"))


# or 

sorted(d,key = lambda x : x.get('age'))