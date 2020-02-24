def f1(a=12,b=5,c=23,*t,**kw):
    s=a+b+c
    for x in t:
        s=s+x
    for n in kw.values():
        s=s+n
    return s
    
def f2(a,b):
    return a+b

ans=f2(b=34,a=56)
print(ans)


s=f1(10,20)
print(s)
s=f1()
print(s)
s=f1(23)
print(s)
s=f1(12,34,56)
print(s)
s=f1(15,2,34,45,56,67,34,x=2,y=4,z=5,d=12,e=7)
print(s)

