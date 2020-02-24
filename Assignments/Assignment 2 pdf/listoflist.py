

lst=[]
ans="y"
while ans=="y":
    ip=int(input("Enter the num you want to add in the list : "))
    i=ip%10
    if i>=len(lst):
        while i>len(lst):
            lst.append([])
        lst.append([ip])
        print(lst)

    else:
        lst[i].append(ip)
        print(lst)
    ans=input("Continue(y/n)")
    
        
    
        
