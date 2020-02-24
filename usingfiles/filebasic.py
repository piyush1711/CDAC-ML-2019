count=1
fh=open(r"myfile1.txt")
fh1=open("mycopy.txt","w")
for ln in fh:
    fh1.write(str(count)+":"+ln)
    print(str(count)+":"+ln,end="")
    count=count+1
fh.close()
fh1.close()
