class Person:
    count=0
    def __init__(self,pid=0,nm="",mob=""):
        Person.count=Person.count+1
        self.__pid=pid
        self.__name=nm
        self.__mobile=mob
    def __str__(self):
        return "Id : "+str(self.__pid)+"\nName:"+self.__name+"\nMobile: "+self.__mobile
    def setMobile(self,m=""):
        self.__mobile=m
    def setName(self,nm=""):
        self.__name=nm
    def setPid(self,pid):
        self.__pid=pid
    def getPid(self):
        return self.__pid
    def getName(self):
        return self.__name
    def getMobile(self):
        return self.__mobile
    
class Employee(Person):
    def __init__(self,pid=0,nm="",mob="",dt="",desg=""):
        Person.__init__(self,pid,nm,mob)
        self.__dept=dt
        self.__desg=desg
    def __str__(self):
        return Person.__str__(self)+"\nDepartment : "+self.__dept+"\nDesignation: "+self.__desg
    def setDept(self,dt=""):
        self.__dept=dt
    def setDesg(self,ds=""):
        self.__desg=ds
    def getDept(self,dt=""):
        return self.__dept
    def getDesg(self,ds=""):
        return self.__desg
    
class SalariedEmp(Employee):
    def __init__(self,pid=0,nm="",mob="",dt="",desg="",s=0.0,b=0.0):
        Employee.__init__(self,pid,nm,mob,dt,desg)
        self.__sal=s
        self.__bonus=b
    def __str__(self):
        return Employee.__str__(self)+"\nSalary : "+str(self.__sal)+"\nBonus : "+str(self.__bonus)
    def calculateSal(self):
        da=0.10*self.__sal
        hra=0.15*self.__sal
        pf=0.08*self.__sal
        return self.__sal+da+hra-pf+self.__bonus
        
    
if __name__=="__main__":
   ''' p=Person(123,"Kishori","11111")
    r=Person(124,"Rajan","22222")
    print(p)
    print(p.count)
    print(r.count)
    print(r)
    p.setMobile("23456656")
    print(p)
   e=Employee(123,"Kishori","11111","Hr","Manager")
   print(e)'''
   e=SalariedEmp(123,"Kishori","11111","Hr","Manager",20000,2000)
   print(e)
   print(e.calculateSal())



