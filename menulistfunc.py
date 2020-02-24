import sys
lst=[]
choice=0

def addlist(num,lst):
    if num>=10 and num<30:
        lst.append(num)
        return True
    else:
        return False

def dellist(num,lst):
    if num in lst:
            print(lst)
            print("Are you sure to delete(y/n)")
            a=input("Select choice :")
            if a=="y":
                lst.remove(num)
                return True
            else:
                return False

def searchlist(num,lst):
    if num in lst:
        n=lst.index(num)
        print("Index of %d is %d" %(num,n))

def modifylist(num,lst):
    if num in lst:
            print(lst)
            print("Are you sure to replace(y/n)")
            a=input("Select choice :")
            if a=="y":
                n=lst.index(num)
                nu=int(input("Enter the new no to be added : "))
                lst[n]=nu
                return True
            else:
                return False
        
            

while choice!=5:
    print("1. Add Data")
    print("2. Delete Data")
    print("3. Search Data")
    print("4. Modify Data")
    print("5. Exit")
    choice=int(input("Enter Choice : "))

    if choice==1:
        num=int(input("Enter Number : "))
        ans=addlist(num,lst)
        
        if ans:
            print("Added Successfully")
        
        else:
            print("Number should be between 10 to 30")
        print(lst)
    elif choice==2:
        print(lst)
        num=int(input("Enter Number to be deleted : "))
        ans=dellist(num,lst)
        if ans:
            print("Deleted Successfully")
        else:
            print("Not Deleted")
         
        print(lst)
        
    elif choice==3:
        num=int(input("Enter Number to be searched : "))
        searchlist(num,lst)
        
    elif choice==4:
        num=int(input("Enter Number to be replaced : "))
        ans=modifylist(num,lst)
        if ans:
            print("Replaced Successfully")
        else:
            print("Not Replaced")
         
        print(lst)
    else:
        sys.exit(0)
