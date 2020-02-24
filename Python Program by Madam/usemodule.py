#import mynodule as m
from mymodule import *
choice=0
while choice!=3:
    print("1. Factorial")
    print("2. Print table")
    print("3. Exit")
    choice=int(input("enter choice"))
    if choice==1:
        num=int(input("Enter number"))
        f=factorial(num)
        print("Factorial ",f)
    elif choice==2:
        num=int(input("Enter number"))
        printTable(num)
        printTable()
    else:
        sys.exit(0)
