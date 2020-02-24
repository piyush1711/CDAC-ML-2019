

choice=0
clist=[12,10,69,45,6]
while choice!=9:
    
    print("1.Accept Data")
    print("2. Delete data by value")
    print("3. delete data by position")
    print("4. sort")
    print("5. reverse")
    print("6. Print in sorted order")
    print("7. print in reverse order")
    print("8. display data")
    
    choice=int(input("Enter the choice : "))

    if choice==1:
        print("a. add at last position")
        print("b. add at given position")
        c=input("Enter choice again :")

        if c=="a":
          data=int(input("Enter data to add : "))
          clist.append(data)
          print(clist)
        elif c=="b":
          pos=int(input("Enter the position: "))
          data=int(input("Enter data to add : "))
          clist.insert(pos,data)
          print(clist)

    if choice==2:
        data=int(input("Enter the data you want to delete :"))
        if data in clist:
            clist.remove(data)
            print("Data deleted successfully")
            print(clist)
        else:
            print("Data not found")

    if choice==3:
        print("a. delete last element")
        print("b. delete from particular position")
        c=input("Enter choice again :")

        if c=="a":
            print(clist)
            clist.pop()
            print("Updated List :")
            
        elif c=="b":    
            print(clist)
            pos=int(input("Enter the postion of data you want to delete : "))
            clist.pop(pos)
            print("Updated List : ",clist)
          
    if choice==4:
        print("a. ascending")
        print("b. descending")
        c=input("Enter choice again :")
        
        if c=="a":
            print(clist)
            clist.sort()
            print("Sorted Ascending List :",clist)
            
        elif c=="b":  
            print(clist)
            clist.sort(reverse=True)
            print("Sorted Descending List : ",clist)

    if choice==5:
        print(clist)
        clist.reverse()
        print("Reversed List :",clist)

    if choice==6:
        pass
    if choice==7:
        pass
    if choice==8:
        print("a. normal")
        print("b. numbered")
        c=input("Enter choice again :")
        
        if c=="a":
            print(clist)
                        
        elif c=="b":
            count=1
            for i in clist:
                print(count,i)
                count=count+1
        
          
              
