# sum 
def add(a):
    sum = 0
    for i in range(a):
        sum = sum+i
    return sum
x = add(10)





# even sum 
def even(b):
    sum2 = 0
    for i in range(b+1):
        if i%2==0:
            sum2 = sum2 + i
    return sum2
y = even(8)



# factorial 
def fec(c,d):
    f=1
    for i in range(c,d+1):
        f=f*i
    return f
z = fec(1,5)



# prime no 
def prime1(num):
    message = ""
    f= 1
    for i in range(2,num):
        if num%i==0:
            f = 0
            break
    if f==0:
        message = "not prime"

    else:
        message = "prime"
    return message
n = prime1(22)

# chota a 
def chota(h):
    c = str(h)
    d = ord(c)
    
    if d > 96:
        e = d-32
    return e
x = chota("a")





def list (j):
    b =[]
    for i in j:
        if i not in b:
            b.append(i)
    return b
u = list([1,2,2,4,5,7,4,6])
print(u)




        









