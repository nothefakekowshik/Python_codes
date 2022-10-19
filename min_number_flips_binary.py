s="110001"
if "1" not in s:
    print(0)
if "0" not in s:
    print(1)
count1,count0=0,0
for i in s:
    if(i=="1"):
        count1+=1
    else:
        count0+=1
