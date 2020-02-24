class A:
    def __init__(self,a1=0,a2=0):
        self.a1=a1
        self.a2=a2
    def __str__(self):
        return "A1 : "+str(self.a1)+" A2 : "+str(self.a2)
class B:
    def __init__(self,b1):
        self.b1=b1
    def __str__(self):
        return " B1: "+str(self.b1) 
class C(A,B):
    def __init__(self,a1=0,a2=0,b1=2,c1=0,c2=0):
        A.__init__(self,a1,a2)
        B.__init__(self,b1)
        self.c1=c1
        self.c2=c2
    def __str__(self):
        return A.__str__(self)+B.__str__(self)+" c1: "+str(self.c1)+" c2: "+str(self.c2)

ob=C(12,13,15,134,23)
print(ob)
    
        
    
