lst=[]
ans="y"
while ans=="y":
    ip=input("enter name u want to add in list ")
    val=ip[1]

    l=len(lst)
    if l==0:
        lst.append(ip)
        
    else:
        for i in lst:
            if i[1]==val:
                temp=lst.index(i)
                lst.insert(temp,ip)
                break
        else:
            lst.append(ip)
    print(lst)
    
    ans=input("continue (y/n)")
    
