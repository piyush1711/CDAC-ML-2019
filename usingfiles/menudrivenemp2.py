import sys
choice=0

fh=open(r"empdata.dat")
lst=fh.readlines()

def displayall():
    for ln in lst:
        x=ln.split(":")
        print("Emp No:",x[0],"Name:",x[1])
    

def displaycond(num):
    for ln in lst:
        x=ln.split(":")
        if int(x[3])>num:
            print("Emp name:",x[1],"Salary:",x[3])

def avgsaldept():
    dic={}
    for ln in lst:
        dep=ln.split(":")[2]
        sal=float(ln.split(":")[3])
        v=dic.get(dep,-1)
        if v!=-1:
            dic[dep][0]=dic[dep][0]+sal
            dic[dep][1]=dic[dep][1]+1
        else:
            dic[dep]=[]
            dic[dep].append(sal)
            dic[dep].append(1)

    for i in dic.keys():
        lst1=dic.get(i)
        print("Average salary of ",i," : ",round(lst1[0]/lst1[1],2))


def sumofsaldesgn():
    dic={}
    for ln in lst:
        des=ln.split(":")[4]
        desgn=des.rstrip("\n")
        sal=float(ln.split(":")[3])
        v=dic.get(desgn,-1)
        if v!=-1:
            dic[desgn]=dic[desgn]+sal          
        else:
            dic[desgn]=sal      

    for i in dic.keys():
        print("Sum of salary of",i,":",dic.get(i))

def avgsalofdesgn():
    dic={}
    for ln in lst:
        des=ln.split(":")[4]
        desgn=des.rstrip("\n")
        sal=float(ln.split(":")[3])
        v=dic.get(desgn,-1)
        if v!=-1:
            dic[desgn][0]=dic[desgn][0]+sal
            dic[desgn][1]=dic[desgn][1]+1
        else:
            dic[desgn]=[]
            dic[desgn].append(sal)
            dic[desgn].append(1)

    for i in dic.keys():
        lst1=dic.get(i)
        print("Average salary of ",i," : ",round(lst1[0]/lst1[1],2))    

while choice!=6:
    print("1. Display empno and name")
    print("2. Display all emp earning > sal")
    print("3. Average salary Deptwise")
    print("4. Designationwise sum of salary")
    print("5. Average salary of designation")
    print("6. Exit")
    choice=int(input("Enter Choice : "))
 
    if choice==1:
        displayall()
    elif choice==2:
        num=int(input("Enter the boundary salary :"))
        displaycond(num)
    elif choice==3:
        avgsaldept()
    elif choice==4:
        sumofsaldesgn()
    elif choice==5:
        avgsalofdesgn()
    else:
        sys.exit(0)


    
