n=int(input("Enter number of days: "))
week=int(input("Enter start of week(0-6): "))

print("S\tM\tT\tW\tT\tF\tS")
if week==0:
    print("",end="")
else:    
    print("\t"*(week-1),end="\t")

j=1
while j<=n:
    print(j,end="\t")
    j=j+1
    week=week+1
    if week==7:
        print()
        week=0
    
