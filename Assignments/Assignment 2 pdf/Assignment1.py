
import sys

string1=input("Enter the String : ")
#string1 = "234567891"

choice=0
while choice!=5:
    print("1. Display characters fro, even Position")
    print("2.Display characters from odd Position")
    print("3. Display Length of a string")
    print("4. Add a at the end of string length times")
    print("5. Exit")
    choice=int(input("Enter the Choice :"))

    if choice==1:
        print("Even position Characters are : ",string1[::2])
    elif choice==2:
        print("Odd position Characters are : ",string1[1::2])
    elif choice==3:
        print("Length of the String : ",len(string1))
    elif choice==4:
        slen=len(string1)
        print(string1+"a"*slen)
    else:
        sys.exit(0)
    
    
