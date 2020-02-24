
def addData(lst):
    empno=int(input("enter employee no :"))
    ename=input("enter employee name :")
    sal=int(input("enter salary of employee :"))
    desg=input("enter designation of name :")
    ans="y"
    ans=input("Confirm Data(y/n)")
    if ans=="y":
        lst.append(str(empno)+":"+ename+":"+str(sal)+":"+desg+"\n")
        return True
    else:
        return False

def displayData(lst):
    for i in lst:
        print(i)

def writeData(lst,mflag,aflag,count):
    if mflag==True:
        if aflag==False:
            print("Hey")
            with open("empdata1.dat","w") as fh:
                for i in lst:
                    fh.write(i)

        else:
            print("-------")
            with open("empdata1.dat","a") as fh:
                for i in lst[count:]:
                    fh.write(i)

    else:
        sys.exit(0)

def searchbyID(lst,eid):
    count=0
    for p in lst:
        id=p.split(":")[0]
        if int(id)==eid:
            return count
        count=count+1
    else:
        return -1

def deleteData(lst,eid):
    pos=searchbyID(lst,eid)
    if pos!=-1:
        print(lst[pos])
        ans=input("Confirm Deletion(y/n)")
        if ans=="y":
            lst.pop(pos)
            return True
    else:
        return False

def modifyData(lst,eid):
    pos=searchbyID(lst,eid)
    if pos!=-1:
        nsal=input("Enter Salary to be modified : ")
        data=lst[pos].split(":")
        print("test:",data)
        data[2]=nsal
        nemp=":".join(data)
        ans=input("Confirm Modification(y/n)")
        if ans=="y":
            lst[pos]=nemp
            print("Modified in list")        
            return True
    else:
        return False
    
    


            

                           
        
    
    
