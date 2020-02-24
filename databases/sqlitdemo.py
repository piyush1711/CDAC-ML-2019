import sqlite3
import sys

def displayAll():
    cursor.execute("select * from mytable")
    for row in cursor.fetchall():
##        print(row)
        print(str(row[0])+","+str(row[1])+","+str(row[2]))

def insertRec():
##    id=11
##    name="Nikhil"
##    sal=10000
    id=int(input("Enter Id : "))
    name=input("Enter name :")
    sal=int(input("Enter Salary : "))

    cursor.execute('''INSERT INTO mytable VALUES(?,?,?)''',(id,name,sal))
##in oracle    cursor.execute('''INSERT INTO mytable VALUES(:id,:name,:sal)''')
    db.commit()

def deleterec():
    id=int(input("Enter id to be deleted"))
    cursor.execute("select * from mytable where id=?",(id,))
    for row in cursor.fetchall():
        print(str(row[0])+","+str(row[1])+","+str(row[2]))
    ans=input("Confirm to delete(y/n)")
    if ans=="y":
        cursor.execute("delete from mytable where id=?",(id,))
        db.commit()
        print("Record deleted Successfully")

def updateRec():
    id=int(input("Enter id to be Updated"))
    sal=int(input("Enter Updated salary"))
    cursor.execute("update mytable set sal=? where id=?",(sal,id))
    db.commit()

def displaybyID():
    id=int(input("Enter id to be Searched"))
    cursor.execute("select * from mytable where id=?",(id,))
    for row in cursor.fetchall():
        print(str(row[0])+","+str(row[1])+","+str(row[2]))
   
    
    
db =sqlite3.connect('mydb1.db')
if db!=None:
    print("Connection done")
else:
    print("Connection not Done")

cursor=db.cursor()

ans="y"
choice=0
while choice!=6:
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Modify Data")
    print("4. Display All")
    print("5. Display by id")
    print("6. Exit")
    choice=int(input("Enter Choice:"))

    if choice==1:
        insertRec()
    elif choice==2:
        deleterec()
    elif choice==3:
        updateRec()
    elif choice==4:
        displayAll()
    elif choice==5:
        displaybyID()
    else:
        sys.exit(0)




