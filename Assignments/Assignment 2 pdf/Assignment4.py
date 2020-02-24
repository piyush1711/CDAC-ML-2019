lst=[]
lo=[]
ch="y"
while ch=="y":
        city=input("enter the city:")
        lst.append(city)
        ch=input("continue to add city(y/n):")

c="y"
while c=="y":
    loc = input("enter the location:")
    lo.append(loc)
    c = input("Continue{y/n):")

print(lst)
print(lo)
for i,j in zip(lst,lo):
    print(i,j)
