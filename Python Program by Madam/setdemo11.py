s=set()
ans="y"
while ans=="y":
    tree=input("enetr tree")
    s.add(tree)
    ans=input("continue(y/n)")
print(s)

s1={3,4,5}
s.update([12,13])
print(s)
s.add(34)
print(s)
for i in s:
    print(i)
#print(s[2:5]) #splicing not allowed in set
fs=frozenset(s)
print(fs)
#fs.add(50) #this is error


