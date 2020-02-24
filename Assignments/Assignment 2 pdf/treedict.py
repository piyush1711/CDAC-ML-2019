import sys
clist={}
choice = 0

def addcitytree():
    cname=input("Enter the city name : ")
    v=clist.get(cname,-1)
    if v==-1:
        tlist=[]
        ans="y"
        while ans=="y":
            tname=input("Enter Tree name : ")
            tlist.append(tname)
            ans=input("Do you want to continue(y/n)")
        clist[cname]=tlist
    else:
        print("City already Present")
    

def displayall():
    for k,v in clist.items():
        print(k,"----->",v)

def displaybykey():
    k=input("Enter the city name : ")
    v=clist.get(k,-1)
    if v!=-1:
        print(clist[k])
    else:
        print("City not found")

def displaybyvalue():
    val=input("Enter name of tree : ")
    for k,v in clist.items():
        if val in v:
            print(k)
def delcity():
    city=input("Enter the name of City to be deleted :")
    v=clist.get(city,-1)
    if v!=-1:
        ans=input("Do you really want to delete(y/n)")
        if ans=="y":
            del(clist[city])
            print("Successfully Deleted")
        else:
            print("Not Deleted")
    else:
        print("City is not present")

def modify():
    cname=input("Enter the City name : ")
    v=clist.get(cname,-1)
    if v!=-1:
        print(v)
        choice=0
        while choice!=4:
            print("1. add in trees list")
            print("2. update tree list")
            print("3. delete from tree list ")
            print("4. exit from modify")
            choice=int(input("Enter the Sub-Choice : "))

            if choice==1:
                tree=input("Enter the tree name :")
                v.append(tree)                
            elif choice==2:
                tree=input("Enter the tree name to be updated :")
                if tree in v:
                    ind=v.index(tree)
                    ntree=input("Enter the new tree name")
                    v[ind]=ntree
                    print(cname,"---->",v)
                
            elif choice==3:
                tree=input("Enter the name of Tree to be deleted :")
                if tree in v:
                    ans=input("Do you really want to delete(y/n)")
                    if ans=="y":
                        v.remove(tree)
                        print("Successfully Deleted")
                    else:
                        print("Not Deleted")
                    
                else:
                    print("Tree not present")
              
                
            else:
                pass
            
    else:
        print("City not present")


while choice!=7: 
    print("1. Enter City Name and trees Name : ")
    print("2. Display Cities and List of all trees")
    print("3. Display list of particular city")
    print("4. Display cities containing tree")
    print("5. Delete City")
    print("6. Modify Tree List")
    print("7. Exit")
    choice=int(input("Enter the Choice : "))

    if choice==1:
        addcitytree()     
    elif choice==2:
        displayall()
    elif choice==3:
        displaybykey()
    elif choice==4:
        displaybyvalue()
    elif choice==5:
        delcity()
    elif choice==6:
        modify()
    else:
        sys.exit(0)
