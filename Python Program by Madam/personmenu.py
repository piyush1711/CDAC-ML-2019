from personclass import Person

def addPerson(lst):
    pid=int(input("Enter pid"))
    nm=input("Enter pname")
    mob=input("Enter mobile")
    p=Person(pid,nm,mob)
    lst.append(p)
    
def displayData(lst):
    for p in lst:
        print(p)
        print("-------------------")
        
def searchById(lst,pid):
    count=0
    for p in lst:
        if p.getPid()==pid:
            return count
        count=count+1
    else:
       return -1
    
def deletePerson(lst,pid):
   pos=searchById(lst,pid)
   if pos!=-1:
       print(plist[pos])
       ans=input("Delete (y/n)")
       if ans=="y":
           plist.pop(pos)
           return True
   else:
       return False
    
def modifyPersonMob(lst,pid,mob):
    pos=searchById(lst,pid)
    if pos!=-1:
        lst[pos].setMobile(mob)
        return True
    else:
        return False
            
    
