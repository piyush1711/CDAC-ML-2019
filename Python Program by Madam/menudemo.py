lst=[]
import sys
def addList(num,lst):
    if num>=10 and num<=30:
        lst.append(num)
        return True
    else:
        return False

    
choice=0

while choice!=5:
    print("1: Add data")
    print("2. Delete Data")
    print("3. search Data")
    print("4 modify data")
    print("5.exit")
    choice=int(input("enter choice"))
    if choice==1:
        num=int(input("enter num"))
        ans=addList(num,lst)
        if ans:
            print("added suuccessfully")
        else:
            print("number should be within range 10 to 30")
        print(lst)
        
    elif choice==2:,
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    else:
        sys.exit(0)
        
