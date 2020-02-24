for i in range(3):
    try:
        num=int(input("Enter Number"))
        num1=int(input("Enter Number"))
        if num1==0:
            raise ZeroDivisionError("Number should be greater than zero")
        d=num/num1
        print(d)
        break
        
    except ZeroDivisionError as e:
        print(e)

    finally:
        print("In Finally Block")

else:
    print("Get lost 3 attempts are over")
