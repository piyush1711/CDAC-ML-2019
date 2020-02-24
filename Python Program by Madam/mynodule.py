def factorial(n):
    print("name : ",__name__)
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact

def printTable(n=5):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

if __name__==" __main__":
    f=factorial(4)
    print(f)
    printTable(3)
    printTable()

