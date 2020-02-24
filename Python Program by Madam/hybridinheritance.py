class A:
    def __init__(self,a1,a2):
        print("in A init")
        self.a1=a1
        self.a2=a2
    def __str__(self):
        print("in A str")
        return "a1: "+str(self.a1)+"a2:"+str(self.a2)
class B(A):
    def __init__(self,b1,**kv):
        print("in B's init",kv)
        super().__init__(**kv)
        self.b1=b1
    def __str__(self):
        print("in B's str") 
        return super().__str__()+"b1:"+str(self.b1)
    
class C(A):
    def __init__(self,c1,c2,**kv):
        print("in C's init",kv)
        super().__init__(**kv)
        self.c1=c1
        self.c2=c2
    def __str__(self):
        print("in c's str") 
        return super().__str__()+"c1:"+str(self.c1) +"c2:"+str(self.c2)

    
class D(B,C):
    def __init__(self,d1,d2,**kv):
       print("in D's init",kv)
       super().__init__(**kv)
       self.d1=d1
       self.d2=d2
    def __str__(self):
       print("in d's str") 
       return super().__str__()+"d1:"+str(self.d1) +"d2:"+str(self.d2) 



ob=D(d1=12,a1=5,a2=3,b1=4,c1=23,c2=25,d2=14)
print("------------------------------------")
print(ob)
