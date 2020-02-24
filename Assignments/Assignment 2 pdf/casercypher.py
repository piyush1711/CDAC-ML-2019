import sys

myKey = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}


choice = 0
while choice != 3:
    print("Menu")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        myStr = input("Enter message to encode: ")
        myStrList = list(myStr)
        print(myStrList)
        myStrEncode = ""

        for i in myStrList:
            if (65<=ord(i) and ord(i)<=90) or (97<=ord(i) and ord(i)<=122):
                for k,v in myKey.items():
                    if i==k:
                        myStrEncode = myStrEncode + v
            else:
                myStrEncode = myStrEncode + i

        print(myStrEncode)
    elif choice == 2:
        myStr = input("Enter message to decode: ")
        myStrList = list(myStr)
        print(myStrList)
        myStrDecode = ""

        for i in myStrList:
            if (65<=ord(i) and ord(i)<=90) or (97<=ord(i) and ord(i)<=122):
                for k,v in myKey.items():
                    if i==v:
                        myStrDecode = myStrDecode + k
            else:
                myStrDecode = myStrDecode + i

        print(myStrDecode)
    else:
        sys.exit(0)
    

