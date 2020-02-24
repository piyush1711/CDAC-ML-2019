def factorial(n):
    print("name : ",__name__)
    print()
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact

def printTable(n=5):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

def prime(n):
    for i in range(2,n):
        if n%i==0:
           return False
           break
        else:
            return True
    

if __name__=="__main__":
    f=factorial(4)
    print(f)
    print()
    printTable(3)
    print()
    printTable()
    print()
    prime(5)

