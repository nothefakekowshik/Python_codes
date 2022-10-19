a=[1,2,2,2,5]
res,count=0,1
for i in range(1,len(a)):
    if(a[i]==a[res]):
        count+=1
    else:
        count-=1
    if(count==0):
        res=i
        count=1
count=0
for i in a:
    if(a[res]==i):
        count+=1
if(count>len(a)//2):
    print(a[res])
else:
    print("-1")