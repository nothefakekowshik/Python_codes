import re
s="hlelo"
a=list(map(str,s))
b=[]
for i in range(len(a)-1):
    if(a[i]!=a[i+1] and a[i]!='l' or a[i]==a[i+1] and a[i]=='l'):
        b.append(a[i])

str_val="".join(b)
pat=r"he(l)*o"
if re.search(pat,str_val):
    print("YES")
else:
    print("NO")