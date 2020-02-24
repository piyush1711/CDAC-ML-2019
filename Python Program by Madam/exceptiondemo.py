for i in range(3):
    try:
        num=int(input("enter number"))
        print("You entered ",num)
        x=int(input("enter number"))
        test={"a":123,"b":345}
        print(test["c"])
        d=num/x
        break
    except (ValueError,KeyError):
        print("pls enter number")
    except ZeroDivisionError:
        print("pls enter nonzero number")
    finally:
        print("in finally block")
        
        
        
