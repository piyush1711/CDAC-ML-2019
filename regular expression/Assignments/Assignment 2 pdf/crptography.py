crypt = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t',
'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T',
'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F',
'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

s1="Pnrfnepvcure? V zhpucersrePnrfnefnynq!"
cipher=""
dicipher=""
s2=input("Enter the String: ")

for i in s2:
    if i.isalpha():
        cipher=cipher+crypt[i]
    else:
        cipher+=i
print("Encoded: ",cipher)

for i in cipher:
    if i.isalpha():
        dicipher+=crypt[i]
    else:
        dicipher+=i
print("Decoded: ",dicipher)
