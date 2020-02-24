'''
import re
s="Something is there somewhere with someone"
##m=re.search("t.*?e",s,re.I|re.M)
m=re.search("s(.*?)e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.span())
    print(m.span(1))
else:
    print("not found")
'''


'''
import re
s="Something is there somewhere with someone"
##m=re.match("s.*?e",s,re.I|re.M)
m=re.match("s(.*)e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.span())
    print(m.span(1))
else:
    print("not found")
'''
'''
import re
s="Something is there somewhere with someone"
m=re.findall("s.*?e",s,re.I|re.M)
if m!=None:
    print(m)
else:
    print("not found")
'''
'''
import re
s="Something is there somewhere with someone"
##lst=re.finditer("s.*?e",s,re.I|re.M)
lst=re.finditer("t(.*?)e",s,re.I|re.M)
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.group(1))
        print(m.span())
        print(m.span(1))
else:
    print("not found")
'''
'''
import re
s="Something is there somewhere with someone"
print(s)
lst=re.sub("s.*?e","any",s,flags=re.I|re.M,count=2)
if lst!=None:
        print(lst)
else:
    print("not found")

'''

import re
s="Something is there somewhere with someone"
print(s)
myreg=re.compile("s.*?e",flags=re.I|re.M)
lst=myreg.search(s)
if lst!=None:
        print(lst.group())
        print(lst.span())
else:
    print("not found")



































