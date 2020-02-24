class Point:
    def __init__(self,a=0,b=0):
        print("init called")
        self.__x=a
        self.__y=b
    def __add__(self,s):
        print("add called")
        if isinstance(s,Point):
            a=self.__x+s.__x
            b=self.__y+s.__y
        else:
            a=self.__x+s
            b=self.__y+s
        return Point(a,b)
    
    def __radd__(self,s):
        print("radd called")
        a=self.__x+s
        b=self.__y+s
        return Point(a,b)
    
    def __sub__(self,s):
        a=self.__x-s.__x
        b=self.__y-s.__y
        return Point(a,b)
        
    def __str__(self):
        print("str called")
        return "x: "+str(self.__x)+" y: "+str(self.__y)


p=Point(23,34)
q=Point(20,30)
print(p)
print(q)
a=p+q
print(a)
c=p-q
a1=p+12
a2=12+q
print(a1)
print(a2)






    
             
