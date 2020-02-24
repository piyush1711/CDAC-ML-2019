import sys
##import mymodule
##import mymodule as m
from mymodule import *

choice=0
while choice!=4:
    print("1. Factorial")
    print("2. Table")
    print("3. Prime")
    print("4. Exit")
    choice=int(input("Enter the Choice : "))

    if choice==1:
        num=int(input("Enter the number : "))
##        f=mymodule.factorial(num)
##        f=m.factorial(num)
        f=factorial(num)
        print("Factorial : ",f)

    elif choice==2:
        num=int(input("Enter the number : "))
##        mymodule.printTable(num)
##        m.printTable(num)
        printTable(num)
        print()
        printTable()
    
    elif choice==3:
        num=int(input("Enter the number : "))
        ans = prime(num)
        if ans:
            print("No is Prime")
        else:
            print("No is not Prime")

    else:
        sys.exit(0)
    

    
