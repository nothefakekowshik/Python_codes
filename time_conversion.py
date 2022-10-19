#12hr to 24hr
s="12:05:45Am"
res=""
ans=[]
h,m,ss=list(map(str,s.split(":")))
if(ss[2:]=="PM"):
    h=int(h)
    if(h<12):
        h+=12
    h=str(h)
    #print("%s:%s:%s" %(h,m,ss[:2]))
else:
    if(h=="12"):
        h="00"
    #print("%s:%s:%s" %(h,m,ss[:2]))
    #res+=h+":"+m+":"+ss[:2]
    #print(res)
    ans.append(h)
    ans.append(m)
    ans.append(ss[:2])
    colon=":"
    print(colon.join(ans))
