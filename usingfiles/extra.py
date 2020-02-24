
with open(r"empdata.dat") as fh:
    for ln in fh:
            x=ln.split(":")
            y=x[3:5][1]
            
            print(y)
    
                

