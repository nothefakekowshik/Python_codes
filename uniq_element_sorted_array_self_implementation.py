a=[1,1,2,2,4]
count=1
for i in range(len(a)-1):
    if(a[i]!=a[i+1]):
        count-=1
    else:
        count+=1
    if(count==0):
        print(a[i])
        break
print(i)    