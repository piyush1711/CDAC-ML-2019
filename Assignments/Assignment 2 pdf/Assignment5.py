
list1=[12,1,3,7,8,5,8]

print(list1[4],list1.index(8))
print(list1[6],list1.index(8))

list2=[]
m = max(list1)

print(m)

for i in range(0,m+1):
    list2.append(-1)

print(list2)

i = 0
for j in list1: 
     list2[j] = i 
     i=i+1

##i = 0
##while i<len(list1):
##     list2[list1[i]] = i
##     i=i+1


print(list2)    
