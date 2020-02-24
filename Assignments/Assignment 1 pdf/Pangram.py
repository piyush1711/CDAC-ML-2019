'''
s="The quick brown fox jumps over the lazy dog."
alphabet = "abcdefghijklmnopqrstuvwxyz"
b=True
for char in alphabet:
    if char in s.lower():
        b=True
    else:
        b=False
        break
if(b):
    print("String is pangram")
else:
    print("Not pangram")
'''

s="The quick brown fox jumps over the lazy dog.#$%$#%"
alphabet = "abcdefghijklmnopqrstuvwxyz"

ss = set("".join(s.split()).lower())
sa = set(alphabet)

print(ss)

if sa.issubset(ss):
    print("String is pangram")
else:
    print("Not pangram")

