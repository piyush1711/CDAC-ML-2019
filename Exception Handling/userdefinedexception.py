from ageexception import AgeException
for i in range(3):
    try:
        pid=int(input("Enter Id : "))
        nm=input("Enter name : ")
        age=int(input("Enter Age :"))
        if age<18 or age>60:
            raise AgeException("Age should be in th range 18 to 60")
        print("You Entered ",pid,nm,age,sep=",")
        break
    except AgeException as e:
        print("In age Exception Block")
        print(e)
