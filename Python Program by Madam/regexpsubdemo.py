import re
s="somethig is there somewhere with someone"
data=re.sub("s.*?e","any",s,flags=re.I,count=0)
print("after substitution:",data)
print("Original:",s)
