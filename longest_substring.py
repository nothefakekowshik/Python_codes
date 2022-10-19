def reversefunc(dooptxt,doopreverse):
    curr_len=0
    for i in range(0,len(dooptxt)):
        lenn=0
        for j in range(i+1,len(doopreverse)):
            if dooptxt[i]==doopreverse[j]:
                lenn+=1
            else:
                continue
        curr_len=max(lenn,curr_len)
    print("length is %d"%(curr_len))
txt=input("enter the string")
revstring=txt[::-1]
#print(revstring)
if(txt==revstring):
    print("Longest substring is %d"%(len(txt)))

else:
    reversefunc(txt,revstring)