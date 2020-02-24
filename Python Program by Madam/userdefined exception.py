from ageexception import AgeException
for i in range(3):
    try:
        id=int(input("enter Id"))
        nm=input("enter name")
        age=int(input("enetr age"))
        if age<18 or age>60:
            raise AgeException("age should be in range 18 to 60")
        print("you entered ",id,nm,age,sep=",")
        break
    except AgeException as e:
        print("in ageexception block")
        print(e)
