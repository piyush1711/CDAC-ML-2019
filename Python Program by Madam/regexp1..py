import re
'''
s="somethig is there somewhere with someone"
lst=re.findall("t.*?e",s,re.I)
if lst!=None:
    print(lst)
else:
    print("not found")'''


s="somethig is there somewhere with someone"
lst=re.finditer("t(.*?)e",s,re.I)
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.span())
        print(m.group(1))
        print(m.span(1))
else:
    print("not found")
