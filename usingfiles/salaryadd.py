sum=0
with open("empdata.dat") as fh:
    for ln in fh:
        x=ln.split(sep=":")
        y=x[3]
        sum=sum+float(y)

    print("Sum of Salary :",sum)
