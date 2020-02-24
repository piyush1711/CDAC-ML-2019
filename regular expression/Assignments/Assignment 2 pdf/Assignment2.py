##string1=input("Enter the String :")
##string2=input("Enter occurance String")
string1="This is cat, cate is cute, where is your cat vdgdsfsdfg"
string2="cat"
count=0
pos=0
while pos!=-1:
    pos=string1.find(string2,pos)
    if pos==-1:
        break
    print("cat position :",pos)
    pos=pos+1
    count=count+1

print("count :"+str(count))


