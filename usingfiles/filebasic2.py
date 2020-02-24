count=1
with open("myfile1.txt") as fh:
    with open("tstcopy.txt","w") as fh1:
        for ln in fh:
            fh1.write(str(count)+":"+ln)
            count=count+1
            
