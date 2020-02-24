#import personclass as p
import sys
from personclass import Person
from personmenu import *

plist=[]
choice=0
while choice!=6:
    print("1. Add new person")
    print("2. delete Person")
    print("3. Modify Person")
    print("4.Display by id")
    print("5. Display all Person")
    print("6. Display by name")
    print("7.Exit")
    choice=int(input("enter choice"))
    if choice==1:
        addPerson(plist)
    elif choice==2:
       pid=int(input("enter pid for search"))
       ans=deletePerson(plist,pid)
       if ans==True:
           print("deleted successfully")
       else:
           print("not found")
    elif choice==3:
        pid=int(input("enter pid for search"))
        mob=input("enter pid for search")
        ans=modifyPersonMob(plist,pid,mob)
        if ans==True:
            print("updated successfully")
        else:
            print("Not found")
    elif choice==4:
       pid=int(input("enter pid for search"))
       pos=searchById(plist,pid)
       if pos!=-1:
           print(plist[pos])
       else:
           print("Not found")
    elif choice==5:
        displayData(plist)
    elif choice==6:
        pass
    
    else:
        sys.exit(0)
        
    
