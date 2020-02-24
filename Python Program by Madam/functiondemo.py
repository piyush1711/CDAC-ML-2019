import sys
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return True
    else:
        return False

def simple(p,n):
    r=0.06
    return p*n*r/100
    

print("1.prime")
print("2.Simple Interest")
print("3. Display Triangle")
print("4.exit")
choice=int(input("Enter choice"))
if choice==1:
    num=int(input("Enter number"))
    ans=prime(num)
    if ans:
        print("not prime")
    else:
        print("prime")
elif choice==2:
    p=float(input("Enter number"))
    n=int(input("Enter number"))
    intrest=simple(p,n)
    print("Interest : ",intrest)
elif choice==3:
    pass
else:
    sys.exit(0)
    


    
