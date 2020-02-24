import pdb
a=12
pdb.set_trace()
b=a
print(id(a))
print(id(b))
print(a,b)
b=b+34
print(id(a))
print(id(b))
print(a,b)
