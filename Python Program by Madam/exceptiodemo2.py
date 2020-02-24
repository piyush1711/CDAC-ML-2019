for i in range(3):
    try:
        num=int(input("enter number"))
        num1=int(input("enter number"))
        if num1==0:
            raise ZeroDivisionError("number should be > 0")
        d=num/num1
        print(d)
        break
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("in finally")
