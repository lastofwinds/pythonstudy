def func(a,b=[]):
    b.append(a)
    return b

v1 = func(1)
v2 = func(2,[])
v3 = func(3)

print(v1,v2,v3)
print(v1)