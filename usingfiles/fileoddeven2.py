count=1
with open("myfile1.txt") as fh:
    with open("tstcopyodd.txt","w") as fh1:
        with open("tstcopyeven.txt","w") as fh2:
            for ln in fh:
                if count%2==0:
                    fh2.write(str(count)+":"+ln)
                    count=count+1
                else:
                    fh1.write(str(count)+":"+ln)
                    count=count+1
            
                    
