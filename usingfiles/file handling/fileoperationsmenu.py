import sys
import os
import filemodule as f

mflag=False
aflag=False
if os.path.exists("empdata1.dat"):
    with open("empdata1.dat") as fh:
        data=fh.readlines()
else:
    data=[]
count=len(data)    

choice=0
while choice!=5:
    print("1. Add data to file")
    print("2. Delete data from file")
    print("3. Modify Data in file")
    print("4. Display Data")
    print("5. Exit")
    choice=int(input("Enter Choice : "))

    if choice==1:
        ans=f.addData(data)
        if ans:
            aflag=True
            mflag=True
            print("aflag set as ",aflag)
        else:
            aflag=False
            mflag=False
    elif choice==2:
        eid=int(input("Enter eid to delete : "))
        ans=f.deleteData(data,eid)
        if ans:
            mflag=True
            print("Deleted Successfully")
        else:            
            print("Not Found")        
    elif choice==3:
        eid=int(input("Enter eid to be modified : "))        
        ans=f.modifyData(data,eid)
        if ans:
            mflag=True
            print("Salary is modified")
        else:
            print("Not Found")
    elif choice==4:
        f.displayData(data)
    else:
        f.writeData(data,mflag,aflag,count)



