text="kowshik"
pat="sh"
k=0
for i in range(len(text)-len(pat)+1):
    c=0
    for j in range(len(pat)):
        if(text[i+j]==pat[j]):
            c+=1
    if(c==len(pat)):
        index=i
        k=1
        break
if(k==1):
    print("Pattern %s is at index %d" %(pat,index))
else:
    print("Pat is not in text")