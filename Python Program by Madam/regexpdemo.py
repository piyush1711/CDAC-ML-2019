import re
'''
s="somethig is there somewhere with someone"
m=re.search("t(.*?)e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
else:
    print("not found")'''



s="somethig is there somewhere with someone"
m=re.match("s(.*)e",s,re.I)
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.span())
    print(m.span(1))
else:
    print("not found")
