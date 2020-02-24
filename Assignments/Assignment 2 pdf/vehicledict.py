import sys
vlist={}
choice = 0
while choice!=8:
    print("1. Enter Person Name and Vehicle Name: ")
    print("2. Delete using key from Dictionary : ")
    print("3. Update value of Key : ")
    print("4. Search vehicle of given Person")
    print("5. Search list of people who has given vehicle")
    print("6. Display all Keys")
    print("7. Display all Values")
    print("8. Exit")
    choice=int(input("enter the Choice : "))

    if choice==1:
        pname=input("Enter Person Name : ")
        v=vlist.get(pname,-1)
        if v==-1:
            vname=input("Enter Vehicle Name : ")
            vlist[pname]=vname
            print(vlist)
        else:
            print("Name already exist")
            print(vlist)
        
    elif choice==2:
        pname=input("Enter key to be deleted : ")
        v=vlist.get(pname,-1)
        if v==-1:
            print(pname,"--->",vlist[pname])
            ans=input("Confirm Deletion(y/n)")
            if ans=="y":
                del(vlist[pname])
                print("Deleted Successfully")
                print(vlist)
            else:
                print("Not Deleted")
        
    elif choice==3:
        pname=input("Enter key to be updated : ")
        v=vlist.get(pname,-1)
        if v==-1:
            print(pname,"--->",vlist[pname])
            nval=input("Enter new value : ")
            ans=input("Confirm Updation(y/n)")
            if ans=="y":
                vlist[pname]=nval
                print("Updated Successfully")
            else:
                print("Not Updated")
        else:
            print("Key not present")
        
    elif choice==4:
        pname=input("Enter key : ")
        v=vlist.get(pname,-1)
        if v!=-1:
            print(pname,"--->",vlist[pname])
        else:
            print("Key is not present")
    elif choice==5:
        val=input("Enter the Key : ")       
        for k,v in vlist.items():
            if v==val:
                print(k,"--->",v)
                

        pass
    elif choice==6:
        for i in vlist.keys():
                print("Key : ",i)
    
    elif choice==7:
        for i in vlist.values():
                print("Values : ",i)
        pass
    else:
        sys.exit(0)

    


