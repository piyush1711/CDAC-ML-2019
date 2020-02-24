##while True:

for i in range(3):
    try:
        num=int(input("Enter Number"))
        print("You entered :",num)
        x=int(input("Enter number"))
        test={"a":123,"b":345}
        print(test["c"])
        d=num/x
        print(d)
        break
    except (ValueError,KeyError):
        print("Pls enter Number")

    except ZeroDivisionError:
        print("pls enter nonzero number :")

##    except:
##        print("Error Occured")
    finally:
        print("In finally Block")

    

    
        
