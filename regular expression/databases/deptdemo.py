import sqlite3
import sys

db = sqlite3.connect('mydb1.db')

if db != None:
    print("Connection done")
else:
    print("Connection Failed")

cursor = db.cursor()

def insertDept():
    dno = 0
    cursor.execute("select max(dno) from dept")
    for row in cursor.fetchone():
        dno = row
    
    dno+=1
    print("Dept No: ",dno)
    dname = input("Enter Dept Name: ")
    location = input("Enter Dept Location: ")
    noofemp = int(input("Enter No of Employee: "))
    
    cursor.execute("insert into dept values(?,?,?,?)",(dno,dname,location,noofemp))
    db.commit()
    
def deleteDept():
    dname = input("Enter Dept Name: ")
    location = input("Enter Dept Location: ")
    cursor.execute("select dname,location from dept where dname=? and location=?",(dname,location))
    
    dname1 = ""
    location1 = ""
    
    row = cursor.fetchone()
    if row != None:
        dname1 = row[0]
        location1 = row[1]
    #print(row)
    #print(type(row))
    
    if dname1 != "" and location1 != "":
        print(dname," ",location," found")
        ans = input("Confirm to delete (y/n)")
        if ans == "y":
            cursor.execute("delete from dept where dname=? and location=?",(dname, location))
            db.commit()
            print("Deleted successfully")
    else:
        print("Invalid ", dname," and ", location)

def updateDept():
    dname = input("Enter Dept Name: ")
    location = input("Enter Dept Location: ")
    noofemp = int(input("Enter No of emp: "))
    cursor.execute("select dname,location from dept where dname=? and location=?",(dname,location))
    
    dname1 = ""
    location1 = ""
    
    row = cursor.fetchone()
    if row != None:
        dname1 = row[0]
        location1 = row[1]
    #print(row)
    #print(type(row))
    
    if dname1 != "" and location1 != "":
        print(dname," ",location," found")
        ans = input("Confirm to update (y/n)")
        if ans == "y":
            cursor.execute("update dept set noofemp=? where dname=? and location=?",(noofemp,dname, location))
            db.commit()
            print("Updated successfully")
    else:
        print("Invalid ", dname," and ", location)



def displayAllDeptByLocation():
    dname = input("Enter Dept Name: ")
    cursor.execute("select dname from dept where dname=?",(dname,))
    
    dname1 = ""  
    
    row = cursor.fetchone()
    if row != None:
        dname1 = row[0]        
    #print(row)
    #print(type(row))
    
    if dname1 != "":
        print(dname," found")           
        cursor.execute("select * from dept where dname=?",(dname,))
        for row in cursor.fetchall():
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])
    else:
        print("Invalid ", dname)
    
def displayAllDept():
    cursor.execute("select distinct(dname) from dept")
    print("Dept Name")
    for row in cursor.fetchall():
        print(row[0])


def showAllDept():
    cursor.execute("select * from dept")
    print("Dno\tDname\tlocation\tnoofemp")
    for row in cursor.fetchall():
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])

while True:
    print("1. Insert Dept")
    print("2. Delete Dept")
    print("3. Update Dept")
    print("4. Display All Dept")
    print("5. Display particular Dept")
    print("6. Display Dept By Location")
    print("7. Show All")    
    print("8. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        insertDept()
    elif choice == 2:
        deleteDept()
    elif choice == 3:
        updateDept()
    elif choice == 4:
        displayAllDept()
    elif choice == 5:
        pass
    elif choice == 6:
        displayAllDeptByLocation()
    elif choice == 7:
        showAllDept()
    else:
        sys.exit(0)
