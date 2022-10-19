import sys
s="the quick brown fox jumps over the lazy dog".strip("")

alphabets="abcdefghijklmnopqrstuvwxyz"
s=s.replace(" ","")

dict={}
curr_max=1000
for i in s:
    curr_max=min(curr_max,ord(i))
print(chr(curr_max))

