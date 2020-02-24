import sys

clist=[]
choice=0
while choice!=5:
    print("1. Add in the list")
    print("2. remove from the list")
    print("3. search for position")
    print("4. serach existance")
    print("5. exit")
    choice=int(input("enter choice"))
    if choice==1:
        ans="y"
        while ans=="y":
            city=input("enter city")
            clist.append(city)
            ans=input("continue(y/n)")
        print(clist)
    elif choice==2:
        print(clist[-1])
        ans=input("do you want to delete it?")
        if ans=="y":
            s=clist.pop()
            print("Deleted successfully",s)
        print(clist)
    elif choice==3:
        city=input("enter city")
        if city in clist:
            pos=clist.index(city)
            print("Found at %d position" %(pos))
    elif choice==4:
       city=input("enter city")
        if city in clist:
            print("city exists")
        else:
            print("city doesnot exists")
    else:
        sys.exit(0)

